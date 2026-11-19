import streamlit as st
import pandas as pd
import os
import plotly.express as px
import base_datos as auth_db
import datos_juego as dj  
from motor_logico import MotorLogicoEgerina
from streamlit_cookies_controller import CookieController
import random
import urllib.request
import urllib.parse

st.set_page_config(page_title="Simulador Psicología", page_icon="🧠", layout="wide", initial_sidebar_state="expanded")
controller = CookieController()
motor_egel = MotorLogicoEgerina()

# Inicialización segura de variables de estado
if "logged_in" not in st.session_state: st.session_state.logged_in = False
if "user_data" not in st.session_state: st.session_state.user_data = None
if "user_id" not in st.session_state: st.session_state.user_id = None
if "caso_activo" not in st.session_state: st.session_state.caso_activo = None
if "indice_pregunta" not in st.session_state: st.session_state.indice_pregunta = 0
if "respuestas_usuario" not in st.session_state: st.session_state.respuestas_usuario = {}
if "mostrar_expediente" not in st.session_state: st.session_state.mostrar_expediente = True
if "caso_guardado_db" not in st.session_state: st.session_state.caso_guardado_db = False
if "pregunta_revisada" not in st.session_state: st.session_state.pregunta_revisada = False
if "tamagotchi_stats" not in st.session_state: st.session_state.tamagotchi_stats = {"hambre": 50, "felicidad": 50, "nivel": 1}

if "psicopesos" not in st.session_state: st.session_state.psicopesos = 50
if "flashcards_usuario" not in st.session_state: st.session_state.flashcards_usuario = []
if "progreso_examenes" not in st.session_state: st.session_state.progreso_examenes = {}
if "progreso_minijuegos" not in st.session_state or not isinstance(st.session_state.progreso_minijuegos, dict):
    st.session_state.progreso_minijuegos = {"dictamen": [], "caos": []}

# Autorreparación en caliente para llaves de minijuegos
if "dictamen" not in st.session_state.progreso_minijuegos:
    st.session_state.progreso_minijuegos["dictamen"] = st.session_state.progreso_minijuegos.pop("triage", [])
if "caos" not in st.session_state.progreso_minijuegos:
    st.session_state.progreso_minijuegos["caos"] = []

# =========================================================================
# FUNCIONES DE GUARDADO Y MOTOR LÓGICO
# =========================================================================
def añadir_exp(monto):
    if st.session_state.user_data is not None:
        nuevo_xp = st.session_state.user_data.get("xp_total", 0) + monto
        nuevo_nivel = min(5, max(1, nuevo_xp // 500 + 1)) # Tope en Nivel 5
        st.session_state.user_data["xp_total"] = nuevo_xp
        st.session_state.user_data["nivel"] = nuevo_nivel
        if st.session_state.logged_in and st.session_state.user_id:
            try:
                auth_db.supabase.table("usuarios").update({
                    "xp_total": nuevo_xp,
                    "nivel": nuevo_nivel
                }).eq("id", st.session_state.user_id).execute()
            except: pass

def actualizar_psicopesos(monto):
    st.session_state.psicopesos += monto
    try: controller.set('simulador_psicopesos', st.session_state.psicopesos)
    except: pass
    if st.session_state.logged_in and st.session_state.user_id:
        try:
            auth_db.supabase.table("usuarios").update({"psicopesos": st.session_state.psicopesos}).eq("id", st.session_state.user_id).execute()
        except: pass

def normalizar_minijuegos(datos_mini):
    if not isinstance(datos_mini, dict): return {"dictamen": [], "caos": []}
    return {
        "dictamen": list(datos_mini.get("dictamen") or datos_mini.get("triage") or []),
        "caos": list(datos_mini.get("caos") or [])
    }

def sincronizar_estado_bd():
    if st.session_state.logged_in and st.session_state.user_id:
        st.session_state.progreso_minijuegos = normalizar_minijuegos(st.session_state.progreso_minijuegos)
        datos_guardar = st.session_state.progreso_examenes.copy()
        datos_guardar["_minijuegos"] = st.session_state.progreso_minijuegos
        try: auth_db.supabase.table("usuarios").update({"estado_examenes": datos_guardar}).eq("id", st.session_state.user_id).execute()
        except: pass
        try: auth_db.supabase.table("usuarios").update({"progreso_minijuegos": st.session_state.progreso_minijuegos}).eq("id", st.session_state.user_id).execute()
        except: pass

def guardar_progreso_actual():
    if st.session_state.caso_activo is not None:
        cid = str(st.session_state.caso_activo)
        st.session_state.progreso_examenes[cid] = {'idx': st.session_state.indice_pregunta, 'respuestas': {str(k): v for k, v in st.session_state.respuestas_usuario.items()}}
        sincronizar_estado_bd()

def guardar_flashcards_directo():
    if st.session_state.logged_in and st.session_state.user_id:
        try: auth_db.supabase.table("usuarios").update({"flashcards": st.session_state.flashcards_usuario}).eq("id", st.session_state.user_id).execute()
        except: pass

def cargar_datos_perfil(datos):
    st.session_state.psicopesos = datos.get("psicopesos") if datos.get("psicopesos") is not None else 50
    st.session_state.flashcards_usuario = datos.get("flashcards") or []
    estado_bd = datos.get("estado_examenes") or {}
    mini_bd = datos.get("progreso_minijuegos") or estado_bd.get("_minijuegos") or {}
    st.session_state.progreso_minijuegos = normalizar_minijuegos(mini_bd)
    st.session_state.progreso_examenes = {k: v for k, v in estado_bd.items() if k != "_minijuegos"}

cookie_user_id = controller.get('simulador_user_id')
if cookie_user_id and not st.session_state.logged_in:
    try:
        perfil = auth_db.supabase.table("usuarios").select("*").eq("id", cookie_user_id).single().execute()
        if perfil.data:
            st.session_state.logged_in = True
            st.session_state.user_id = cookie_user_id
            st.session_state.user_data = perfil.data
            cargar_datos_perfil(perfil.data)
    except: pass

@st.cache_data
def cargar_reactivos():
    if os.path.exists("banco_preguntas_egel_final.csv"): return pd.read_csv("banco_preguntas_egel_final.csv", encoding='utf-8-sig')
    elif os.path.exists("banco_preguntas.csv"): return pd.read_csv("banco_preguntas.csv", encoding='utf-8-sig')
    return pd.DataFrame()
df_reactivos = cargar_reactivos()

# =========================================================================
# BARRA LATERAL VISUAL, ECONOMÍA Y FEEDBACK
# =========================================================================
with st.sidebar:
    st.markdown("### 🎨 Personalización Libre")
    c1, c2, c3 = st.columns(3)
    color_fondo = c1.color_picker("Fondo", "#0b1120")
    color_tarjeta = c2.color_picker("Tarjetas", "#1e293b")
    color_primario = c3.color_picker("Letras y Bordes", "#38bdf8")
    tema = {'bg': color_fondo, 'card_bg': color_tarjeta, 'primary': color_primario, 'glow': f"{color_primario}66", 'text': "#f8fafc"}

    css_global = f"""
    <style>
    [data-testid="stAppViewContainer"] {{ background-color: {tema['bg']} !important; }}
    [data-testid="stHeader"] {{ background-color: transparent !important; }}
    [data-testid="stSidebar"] {{ background-color: {tema['card_bg']} !important; border-right: 2px solid {tema['primary']} !important; }}
    div.stButton > button {{ border: 1px solid {tema['primary']} !important; background-color: {tema['card_bg']} !important; color: {tema['text']} !important; transition: all 0.3s ease !important; border-radius: 8px !important; }}
    div.stButton > button:hover {{ box-shadow: 0 0 15px {tema['glow']} !important; background-color: {tema['primary']} !important; color: {tema['bg']} !important; }}
    [data-testid="stTabs"] button {{ color: {tema['text']} !important; }}
    [data-testid="stTabs"] button[aria-selected="true"] {{ border-bottom-color: {tema['primary']} !important; color: {tema['primary']} !important; text-shadow: 0 0 10px {tema['glow']} !important; }}
    h1, h2, h3 {{ color: {tema['primary']} !important; text-shadow: 0 0 10px {tema['glow']}; }}
    .hp-bar-container {{ width: 100%; background: {tema['card_bg']}; border-radius: 10px; border: 2px solid {tema['primary']}; height: 25px; margin-bottom: 15px; overflow: hidden; box-shadow: 0 0 10px {tema['glow']};}}
    .hp-bar-fill {{ height: 100%; transition: width 0.3s; display: flex; align-items: center; justify-content: flex-end; padding-right: 10px; font-weight: bold; color: white; text-shadow: 1px 1px 2px black; }}
    .mem-btn {{ min-height: 120px; font-size: 16px; font-weight: bold; border-radius: 10px; border: 2px solid {tema['primary']}; background-color: {tema['bg']}; transition: all 0.3s; display: flex; align-items: center; justify-content: center; text-align: center; padding: 10px; color: {tema['text']}; box-shadow: 0 0 8px {tema['glow']};}}
    .mem-btn-flipped {{ background-color: {tema['primary']}; color: {tema['bg']}; border-color: {tema['text']}; }}
    .mem-btn-matched {{ background-color: #22c55e; color: #064e3b; border-color: #16a34a; opacity: 0.8; }}
    </style>
    """
    st.markdown(css_global, unsafe_allow_html=True)
    st.markdown("---")

    perfil = st.session_state.user_data
    nombre = perfil.get('username', 'Sustentante') if perfil else "Sustentante"
    xp_actual = perfil.get('xp_total', 0) if perfil else 0
    nivel = min(5, max(1, xp_actual // 500 + 1))
    # ... tu código de Personalización Libre ...

    # Sistema de 5 Niveles y Rangos Oficiales (con 4 espacios de sangría)
    if xp_actual >= 5000:
        nivel = 5
        halo_color = "#fbbf24"
        rango_text = "✨ Sustentante Élite"
        xp_sig = 5000
        progreso = 1.0
    elif xp_actual >= 3000:
        nivel = 4
        halo_color = "#a855f7"
        rango_text = "🔮 Sustentante Avanzado Élite"
        xp_sig = 5000
        progreso = max(0.0, min((xp_actual - 3000) / 2000.0, 1.0))
    elif xp_actual >= 1500:
        nivel = 3
        halo_color = "#8b5cf6"
        rango_text = "🔮 Sustentante Avanzado"
        xp_sig = 3000
        progreso = max(0.0, min((xp_actual - 1500) / 1500.0, 1.0))
    elif xp_actual >= 500:
        nivel = 2
        halo_color = "#0ea5e9"
        rango_text = "🛡️ Sustentante Novato Avanzado"
        xp_sig = 1500
        progreso = max(0.0, min((xp_actual - 500) / 1000.0, 1.0))
    else:
        nivel = 1
        halo_color = "#38bdf8"
        rango_text = "🛡️ Sustentante Novato"
        xp_sig = 500
        progreso = max(0.0, min(xp_actual / 500.0, 1.0))

    bg_avatar = f"linear-gradient(135deg, {tema['bg']}, {tema['card_bg']})"

    st.markdown(f"""
    <div style='background: {bg_avatar}; padding: 15px; border-radius: 12px; border: 2px solid {halo_color}; box-shadow: 0 0 20px {halo_color}40; text-align: center; margin-bottom: 10px;'>
        <h2 style='margin:0; color: white; text-shadow: 0 2px 4px rgba(0,0,0,0.5);'>👤 {nombre}</h2>
        <p style='margin:5px 0 0 0; color: {halo_color}; font-weight: bold; letter-spacing: 0.5px;'>{rango_text} (Nv.{nivel}/5)</p>
    </div>
    <div style='background: {tema["card_bg"]}; padding: 10px; border-radius: 8px; text-align: center; border: 1px solid {tema["primary"]}; margin-bottom: 20px;'>
        <h3 style='margin:0; color: {tema["primary"]};'>💰 {st.session_state.psicopesos}</h3>
    </div>
    """, unsafe_allow_html=True)
    
    texto_barra = f"EXP: {xp_actual} (Nivel Máximo)" if nivel == 5 else f"EXP: {xp_actual} / {xp_sig}"
    st.progress(progreso, text=texto_barra)
    st.markdown("---")
    st.markdown("### 🏅 Tus Emblemas")
    if perfil:
        for emblema in auth_db.obtener_emblemas_usuario(st.session_state.user_id): st.markdown(f"- {emblema}")
    st.markdown("---")
            
    if st.button("Cerrar Sesión", use_container_width=True): 
        try: controller.remove('simulador_user_id')
        except: pass
        try: controller.remove('simulador_psicopesos')
        except: pass
        st.session_state.clear()
        st.rerun()

    # --- FEEDBACK / REPORTE DE ERRORES POR GMAIL (SMTP) ---
    st.markdown("---")
    with st.expander("🛠️ Reportar Error o Feedback"):
        tipo_seccion = st.selectbox("Sección afectada:", ["Simulacro / Pregunta", "Minijuego", "General"])
        tipo_problema = st.selectbox("Tipo de detalle:", [
            "Error en la respuesta correcta", 
            "Error teórico / conceptual", 
            "Reactivo poco claro / confuso", 
            "Error de redacción o escritura", 
            "Demasiado fácil / difícil", 
            "Otro"
        ])
        detalle_comentario = st.text_area("Describe el detalle o número de reactivo:")
        
        if st.button("Enviar Reporte", use_container_width=True):
            if detalle_comentario.strip():
                import smtplib
                from email.mime.text import MIMEText

                try:
                    remitente = st.secrets["EMAIL_EMISOR"]
                    clave_app = st.secrets["EMAIL_PASS"]
                    usuario_reporta = perfil.get("username", "Sustentante") if perfil else "Anónimo"

                    cuerpo = (
                        f"Usuario: {usuario_reporta}\n"
                        f"Sección: {tipo_seccion}\n"
                        f"Tipo de detalle: {tipo_problema}\n\n"
                        f"Comentario:\n{detalle_comentario}"
                    )

                    msg = MIMEText(cuerpo, "plain", "utf-8")
                    msg["Subject"] = f"🚨 Feedback Simulador EGEL: {tipo_seccion}"
                    msg["From"] = remitente
                    msg["To"] = remitente  # Te lo envías a ti mismo

                    with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=10) as server:
                        server.login(remitente, clave_app)
                        server.send_message(msg)

                    st.success("¡Reporte enviado a tu correo con éxito!")
                except Exception as e:
                    st.error(f"No se pudo enviar el correo: {e}")
            else:
                st.warning("Escribe una breve descripción antes de enviar.")

# =========================================================================
# PANTALLA DE LOGIN
# =========================================================================
if not st.session_state.logged_in:
    st.markdown("<h1 style='text-align: center;'>🧠 Simulador Psicología</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        tab1, tab2 = st.tabs(["🔑 Iniciar Sesión", "📝 Registrarse"])
        with tab1:
            with st.form("form_login"):
                email_login = st.text_input("Correo Electrónico")
                pass_login = st.text_input("Contraseña", type="password")
                if st.form_submit_button("Verificar Credenciales", use_container_width=True):
                    exito, usuario_auth, datos = auth_db.iniciar_sesion(email_login, pass_login)
                    if exito:
                        controller.set('simulador_user_id', usuario_auth.id)
                        st.session_state.user_id = usuario_auth.id
                        st.session_state.user_data = datos
                        cargar_datos_perfil(datos)
                        st.session_state.logged_in = True 
                        st.rerun()
                    else: st.error(datos)
        with tab2:
            with st.form("form_registro"):
                user_reg = st.text_input("Nombre de Usuario")
                email_reg = st.text_input("Correo Electrónico")
                pass_reg = st.text_input("Contraseña", type="password")
                if st.form_submit_button("Crear Cuenta", type="primary", use_container_width=True):
                    exito, mensaje = auth_db.registrar_usuario(email_reg, pass_reg, user_reg)
                    if exito: st.success(mensaje)
                    else: st.error(mensaje)
    if st.session_state.logged_in:
        st.success("✅ Entorno clínico asegurado.")
        if st.button("🚀 Iniciar Servidor", type="primary", use_container_width=True): st.rerun()
    else: st.stop()

# =========================================================================
# VISTAS PRINCIPALES
# =========================================================================
if st.session_state.caso_activo is None:
    t_ex, t_met, t_prac, t_tama = st.tabs(["📚 Simulacros", "📊 Estadísticas", "🎮 Minijuegos", "🐾 Mascota"])

    with t_ex:
        def cargar_examen(id_examen):
            st.session_state.caso_activo = id_examen
            prog = st.session_state.progreso_examenes.get(str(id_examen)) or {'idx': 0, 'respuestas': {}}
            st.session_state.indice_pregunta = prog.get('idx', 0)
            st.session_state.respuestas_usuario = {int(k): v for k, v in prog.get('respuestas', {}).items()}
            st.session_state.pregunta_revisada = False
            st.session_state.caso_guardado_db = False
            st.rerun()

        def etiqueta_boton(id_examen, texto_base):
            prog = st.session_state.progreso_examenes.get(str(id_examen))
            if prog and len(prog.get('respuestas', {})) > 0:
                return f"{texto_base} (En curso: P.{prog.get('idx', 0) + 1})"
            return texto_base

        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.markdown("#### 🟡 Evaluación")
            if st.button(etiqueta_boton(1, "Caso Clínico 1"), use_container_width=True): cargar_examen(1)
            if st.button(etiqueta_boton(2, "Caso Clínico 2"), use_container_width=True): cargar_examen(2)
        with c2:
            st.markdown("#### 🟢 Intervención")
            if st.button(etiqueta_boton(3, "Caso Clínico 3"), use_container_width=True): cargar_examen(3)
            if st.button(etiqueta_boton(4, "Caso Clínico 4"), use_container_width=True): cargar_examen(4)
            if st.button(etiqueta_boton(5, "Caso Clínico 5"), use_container_width=True): cargar_examen(5)
        with c3:
            st.markdown("#### 🔴 Investigación")
            if st.button(etiqueta_boton(6, "Estudio 1"), use_container_width=True): cargar_examen(6)
            if st.button(etiqueta_boton(7, "Estudio 2"), use_container_width=True): cargar_examen(7)
            if st.button(etiqueta_boton(8, "Estudio 3"), use_container_width=True): cargar_examen(8)
        with c4:
            st.markdown("#### 🟣 Transversal (Lenguaje y Comunicación)")
            if st.button(etiqueta_boton(9, "Lectura 1"), use_container_width=True): cargar_examen(9)
            if st.button(etiqueta_boton(10, "Lectura 2"), use_container_width=True): cargar_examen(10)
            if st.button(etiqueta_boton(11, "Lectura 3"), use_container_width=True): cargar_examen(11)
            if st.button(etiqueta_boton(12, "Lectura 4"), use_container_width=True): cargar_examen(12)

    with t_met:
        historial = auth_db.obtener_progreso_usuario(st.session_state.user_id)
        if not historial: st.info("Completa un caso para ver estadísticas.")
        else:
            mapa = {1:"Evaluación", 2:"Evaluación", 3:"Intervención", 4:"Intervención", 5:"Intervención", 6:"Investigación", 7:"Investigación", 8:"Investigación", 9:"Transversal", 10:"Transversal", 11:"Transversal", 12:"Transversal"}
            datos = {"Evaluación": [], "Intervención": [], "Investigación": [], "Transversal": []}
            for h in historial: datos[mapa.get(h["caso_id"], "Transversal")].append((h["aciertos"] / h["total_preguntas"]) * 100)
            promedios = [sum(datos[a])/len(datos[a]) if datos[a] else 0 for a in list(datos.keys())]
            fig = px.line_polar(pd.DataFrame(dict(r=promedios, theta=list(datos.keys()))), r='r', theta='theta', line_close=True, range_r=[0,100], markers=True)
            fig.update_traces(fill='toself', fillcolor=tema['glow'], line_color=tema['primary'])
            fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color=tema['text']))
            st.plotly_chart(fig, use_container_width=True)

    with t_tama:
        c_pet, c_store = st.columns([1, 1.5])
        ts = st.session_state.tamagotchi_stats
        with c_pet:
            emo = "🐱" if ts["hambre"] > 40 and ts["felicidad"] > 40 else "🐱💤" if ts["hambre"] <= 20 else "🐱💔"
            st.markdown(f"<div style='font-size: 100px; text-align: center; padding: 20px; background: {tema['card_bg']}; border-radius: 15px; border: 2px solid {tema['primary']}; box-shadow: 0 0 15px {tema['glow']};'>{emo}</div>", unsafe_allow_html=True)
            st.write("**Hambre:**"); st.progress(ts["hambre"]/100.0)
            st.write("**Felicidad:**"); st.progress(ts["felicidad"]/100.0)
        with c_store:
            st.subheader("🏪 Tienda")
            c1, c2 = st.columns(2)
            with c1:
                with st.container(border=True):
                    st.write("🐟 **Comida** (Satisfacción +20)")
                    if st.button("Comprar 💰 10"):
                        if st.session_state.psicopesos >= 10: actualizar_psicopesos(-10); ts["satisfacción"] = min(100, ts["satisfacción"]+20); st.rerun()
                        else: st.error("Sin saldo")
            with c2:
                with st.container(border=True):
                    st.write("🧶 **Juguete** (Fel. +30)")
                    if st.button("Comprar 💰 25"):
                        if st.session_state.psicopesos >= 25: actualizar_psicopesos(-25); ts["felicidad"] = min(100, ts["felicidad"]+30); st.rerun()
                        else: st.error("Sin saldo")

    with t_prac:
        modo_juego = st.radio("Filtro de Especialidad:", ["Evaluación Psicológica", "Intervención", "Investigación", "Modo Caótico (Todas)"], horizontal=True)
        tm, tj, tc = st.tabs(["🎴 Memorama Clínico", "⚖️ Dictamen Exprés", "🌪️ Caos Conceptual"])

        with tm:
            st.info("ℹ️ **Instrucciones:** Empareja los conceptos clínicos. Las parejas que descubras se guardarán en tu Bóveda personal.")
            c_juego, c_bov = st.columns([2, 1])
            with c_juego:
                if "memorama" not in st.session_state:
                    sel = random.sample(dj.TODAS_LAS_FLASHCARDS, min(6, len(dj.TODAS_LAS_FLASHCARDS))); crts = []
                    for c in sel:
                        crts.append({"id": c["id"], "texto": c["front"]}); crts.append({"id": c["id"], "texto": c["back"]})
                    random.shuffle(crts); st.session_state.memorama = {"cartas": crts, "volteadas": [], "emparejadas": [], "bloqueado": False}
                mem = st.session_state.memorama
                if len(mem["emparejadas"]) == len(mem["cartas"]):
                    st.success("🎉 ¡Tablero despejado! +20 💰 y +15 EXP.")
                    if st.button("Recoger Recompensa", type="primary", key="btn_mem"):
                        actualizar_psicopesos(20)
                        añadir_exp(15)
                        del st.session_state.memorama
                        st.rerun()
                else:
                    cols = st.columns(3)
                    for i, carta in enumerate(mem["cartas"]):
                        col = cols[i % 3]
                        if i in mem["emparejadas"]: col.markdown(f"<div class='mem-btn mem-btn-matched'>✓ {carta['texto']}</div><br>", unsafe_allow_html=True)
                        elif i in mem["volteadas"]: col.markdown(f"<div class='mem-btn mem-btn-flipped'>{carta['texto']}</div><br>", unsafe_allow_html=True)
                        else:
                            if col.button("❓ Revelar", key=f"mem_{i}", use_container_width=True, disabled=mem["bloqueado"]):
                                mem["volteadas"].append(i)
                                if len(mem["volteadas"]) == 2:
                                    carta1 = mem["cartas"][mem["volteadas"][0]]; carta2 = mem["cartas"][mem["volteadas"][1]]
                                    if carta1["id"] == carta2["id"]: 
                                        mem["emparejadas"].extend(mem["volteadas"]); mem["volteadas"] = []
                                        if carta1["id"] not in st.session_state.flashcards_usuario:
                                            st.session_state.flashcards_usuario.append(carta1["id"])
                                            guardar_flashcards_directo()
                                            st.toast("🔓 ¡Flashcard desbloqueada en tu Bóveda!", icon="📚")
                                    else: mem["bloqueado"] = True
                                st.rerun()
                    if mem["bloqueado"] and st.button("Ocultar Error", use_container_width=True):
                        mem["volteadas"] = []; mem["bloqueado"] = False; st.rerun()
            with c_bov:
                st.markdown("### 📚 Bóveda")
                st.write(f"Desbloqueadas: **{len(st.session_state.flashcards_usuario)} / {len(dj.TODAS_LAS_FLASHCARDS)}**")
                mostrar_todas = st.toggle("👁️ Revelar todas las Flashcards", value=False)
                with st.expander("Ver Cartas de la Bóveda", expanded=True):
                    for fc in dj.TODAS_LAS_FLASHCARDS:
                        if fc["id"] in st.session_state.flashcards_usuario or mostrar_todas: st.success(f"**{fc['front']}**\n\n{fc['back']}")
                        else: st.markdown("<div style='opacity:0.4; padding:8px; border:1px solid gray; border-radius:6px; margin-bottom:6px;'>🔒 <i>Bloqueada (Encuéntrala en el Memorama)</i></div>", unsafe_allow_html=True)

        with tj:
            st.info("ℹ️ **Instrucciones:** Selecciona el diagnóstico idóneo. Ganas +2 💰 y +5 EXP por cada acierto inmediato.")
            bf = [c for c in dj.BANCO_NARRATIVO if modo_juego == "Modo Caótico (Todas)" or c["area"] == modo_juego]
            if len(bf) < 1: st.warning("No hay suficientes casos. Prueba Modo Caótico.")
            else:
                if "partida_rpg" not in st.session_state or st.session_state.get("um_rpg") != modo_juego:
                    sel = random.sample(bf, min(5, len(bf))); rd = []
                    for s in sel:
                        opcs = s["distractores"].copy(); opcs.append(s["respuesta"]); random.shuffle(opcs)
                        rd.append({"d": s["dialogo"], "r": s["respuesta"], "o": opcs})
                    st.session_state.partida_rpg = {"rondas": rd, "idx": 0, "vidas": 3, "aciertos": 0, "go": False, "vic": False}; st.session_state.um_rpg = modo_juego
                jr = st.session_state.partida_rpg
                st.markdown(f"<div class='hp-bar-container'><div class='hp-bar-fill' style='width: {(jr['vidas']/3)*100}%; background: {'#22c55e' if jr['vidas']==3 else '#eab308' if jr['vidas']==2 else '#ef4444'}; color: #000;'>HP {jr['vidas']}/3</div></div>", unsafe_allow_html=True)
                
                if not jr["go"] and not jr["vic"]:
                    ra = jr["rondas"][jr["idx"]]
                    st.markdown(f"<div style='background: {tema['card_bg']}; padding: 20px; border-left: 5px solid {tema['primary']}; font-style: italic; border-radius: 5px; box-shadow: 0 0 10px {tema['glow']};'>🗣️ {ra['d']}</div><br>", unsafe_allow_html=True)
                    el = st.radio("Opciones:", ra["o"], key=f"rad_rpg_{jr['idx']}")
                    if st.button("⚖️ Confirmar", type="primary"):
                        if ra["r"] == el:
                            st.toast("✅ ¡Acierto! Ganaste +2 💰 y +5 EXP", icon="🪙")
                            actualizar_psicopesos(2)
                            añadir_exp(5)
                            registro = f"{ra['d'][:55]}... ➡️ {ra['r']}"
                            lista_dictamen = st.session_state.progreso_minijuegos.setdefault("dictamen", [])
                            if registro not in lista_dictamen:
                                lista_dictamen.append(registro)
                                sincronizar_estado_bd()
                            jr["aciertos"] += 1; jr["idx"] += 1
                            if jr["aciertos"] == len(jr["rondas"]): jr["vic"] = True
                        else:
                            st.toast("❌ Incorrecto. Perdiste 1 vida", icon="💔"); jr["vidas"] -= 1; jr["go"] = (jr["vidas"] <= 0)
                        st.rerun()
                elif jr["vic"]:
                    st.success("🎉 ¡Nivel Superado! +30 💰 y +20 EXP.")
                    if st.button("Cobrar Recompensa", type="primary"):
                        actualizar_psicopesos(30)
                        añadir_exp(20)
                        del st.session_state.partida_rpg
                        st.rerun()
                elif jr["go"]:
                    st.error("💀 Error clínico. Perdiste todas tus vidas.")
                    if st.button("Volver a Intentarlo", type="primary"): del st.session_state.partida_rpg; st.rerun()
                
                resueltos_d = st.session_state.progreso_minijuegos.get("dictamen", [])
                if resueltos_d:
                    with st.expander(f"📚 Casos dominados en Dictamen Exprés ({len(resueltos_d)})"):
                        for r in resueltos_d: st.markdown(f"- ✅ {r}")

        with tc:
            st.info("ℹ️ **Instrucciones:** Selecciona las características que pertenecen al Objetivo azul.")
            dif = st.radio("Conceptos a encontrar:", [2, 3, 4], index=2, horizontal=True)
            cf = {k: v for k, v in dj.DATOS_CAOS.items() if modo_juego == "Modo Caótico (Todas)" or v["area"] == modo_juego}
            if len(cf) < 2: st.warning("Elige 'Modo Caótico' para tener suficientes datos.")
            else:
                if "partida_caos" not in st.session_state or st.session_state.get("um_caos") != modo_juego or st.session_state.get("udif") != dif:
                    obj = random.choice(list(cf.keys())); cor = random.sample(cf[obj]["correctos"], dif); dis = []
                    for k, v in dj.DATOS_CAOS.items():
                        if k != obj: dis.extend(v["correctos"])
                    tab = cor + random.sample(dis, 12 - dif); random.shuffle(tab)
                    st.session_state.partida_caos = {"obj": obj, "tab": tab, "cor": cor, "enc": [], "err": 0, "max": 3, "vic": False, "go": False}; st.session_state.um_caos = modo_juego; st.session_state.udif = dif
                c = st.session_state.partida_caos
                st.markdown(f"<div class='hp-bar-container'><div class='hp-bar-fill' style='width: {((3-c['err'])/3)*100}%; background: {'#22c55e' if c['err']==0 else '#eab308' if c['err']==1 else '#ef4444'}; color: #000;'>HP {3-c['err']}/3</div></div>", unsafe_allow_html=True)
                st.markdown(f"### 🎯 Objetivo: {c['obj']}")
                if c["vic"]:
                    pago = 10 + (dif * 5)
                    st.success(f"🏆 ¡Tablero despejado! +{pago} 💰 y +{pago} EXP.")
                    if st.button("Cobrar recompensa", type="primary", key="btn_caos"): 
                        actualizar_psicopesos(pago)
                        añadir_exp(pago)
                        lista_caos = st.session_state.progreso_minijuegos.setdefault("caos", [])
                        if c["obj"] not in lista_caos:
                            lista_caos.append(c["obj"])
                            sincronizar_estado_bd()
                        del st.session_state.partida_caos; st.rerun()
                elif c["go"]:
                    st.error(f"💀 Demasiados errores. Los correctos eran: {', '.join(c['cor'])}")
                    if st.button("Reintentar", type="primary"): del st.session_state.partida_caos; st.rerun()
                else:
                    cols = st.columns(4)
                    for i, cpt in enumerate(c['tab']):
                        col = cols[i % 4]
                        if cpt in c['enc']:
                            if cpt in c['cor']: col.success(f"✅ {cpt}")
                            else: col.error(f"❌ {cpt}")
                        else:
                            if col.button(cpt, key=f"bc_{i}", use_container_width=True):
                                c["enc"].append(cpt)
                                if cpt not in c["cor"]: c["err"] += 1; c["go"] = (c["err"] >= c["max"])
                                else: c["vic"] = (len([x for x in c["enc"] if x in c["cor"]]) == dif)
                                st.rerun()
                resueltos_c = st.session_state.progreso_minijuegos.get("caos", [])
                if resueltos_c:
                    with st.expander(f"🌪️ Conceptos dominados en Caos Conceptual ({len(resueltos_c)})"):
                        st.markdown(", ".join([f"✅ **{x}**" for x in resueltos_c]))

else:
    # MODO EXAMEN
    cid = st.session_state.caso_activo
    q_df = df_reactivos[df_reactivos["id_reactivo"] == cid].reset_index(drop=True)
    total = len(q_df); idx = st.session_state.indice_pregunta

    st.title(f"Simulación en Progreso: {dj.CASOS_CLINICOS[cid]['titulo']}")
    col_p, col_b = st.columns([3, 1])
    col_p.progress(min((idx + 1) / max(total, 1), 1.0))
    col_p.write(f"**Reactivo {min(idx + 1, total)} de {total}**")
    
    if col_b.button("🚪 Abandonar Examen", use_container_width=True): 
        guardar_progreso_actual()
        st.session_state.caso_activo = None; st.rerun()

    if st.button("Ocultar/Ver Caso", use_container_width=True):
        st.session_state.mostrar_expediente = not st.session_state.mostrar_expediente; st.rerun()

    if st.session_state.mostrar_expediente:
        c_lec, c_reac = st.columns([1.2, 1], gap="large")
        with c_lec: st.markdown("### 📁 Lectura"); st.container(border=True).markdown(dj.CASOS_CLINICOS[cid]["texto"])
    else: c_reac = st.container()

    with c_reac:
        if idx < total:
            fila = q_df.iloc[idx]; st.markdown(f"### 📝 Reactivo\n**{fila['pregunta']}**")
            ops = [fila["opcion_a"], fila["opcion_b"], fila["opcion_c"]]
            prev = st.session_state.respuestas_usuario.get(idx, None)
            eleccion = st.radio("Selecciona:", options=ops, index=ops.index(prev) if prev in ops else None, disabled=st.session_state.pregunta_revisada)
            
            col_nav1, col_nav2 = st.columns(2)
            
            if not st.session_state.pregunta_revisada:
                if col_nav1.button("⬅️ Pregunta Anterior", disabled=(idx == 0)):
                    if idx > 0:
                        st.session_state.indice_pregunta -= 1
                        guardar_progreso_actual()
                        st.rerun()
                
                if col_nav2.button("Revisar Respuesta 🧐", type="primary"):
                    if eleccion: 
                        st.session_state.respuestas_usuario[idx] = eleccion; st.session_state.pregunta_revisada = True
                        guardar_progreso_actual()
                        st.rerun()
                    else: st.warning("Selecciona una opción.")
            else:
                if eleccion[0] == fila["respuesta_correcta"]: st.success("✅ **¡Correcto!**")
                else: st.error(f"❌ **Incorrecto.** La correcta era la **{fila['respuesta_correcta']}**.")
                st.container(border=True).caption(f"💡 **Justificación:** {fila['justificacion_egerina']}")
                
                if col_nav1.button("⬅️ Pregunta Anterior", disabled=(idx == 0)):
                    if idx > 0:
                        st.session_state.indice_pregunta -= 1
                        st.session_state.pregunta_revisada = False
                        guardar_progreso_actual()
                        st.rerun()

                if col_nav2.button("Siguiente Pregunta ➡️" if idx < total - 1 else "Ver Resultados Finales 🏁", type="primary"):
                    st.session_state.indice_pregunta += 1; st.session_state.pregunta_revisada = False
                    guardar_progreso_actual()
                    st.rerun()
        else:
            st.success("🎉 ¡Completado!")
            aciertos = sum([1 for i in range(total) if st.session_state.respuestas_usuario.get(i, "N")[0] == q_df.iloc[i]["respuesta_correcta"]])
            
            puntaje_icne = motor_egel.calcular_icne_mision(aciertos, total)
            categoria_egel, xp_ganada = motor_egel.evaluar_desempeno(puntaje_icne)

            if not st.session_state.caso_guardado_db:
                auth_db.guardar_progreso_caso(st.session_state.user_id, cid, aciertos, total, 120, 0)
                añadir_exp(xp_ganada)
                actualizar_psicopesos(50)
                st.session_state.caso_guardado_db = True
                if str(cid) in st.session_state.progreso_examenes:
                    del st.session_state.progreso_examenes[str(cid)]
                    sincronizar_estado_bd()
            
            c1, c2, c3 = st.columns(3)
            c1.metric("Aciertos", f"{aciertos} / {total}")
            c2.metric("Puntaje ICNE", f"{puntaje_icne} pts")
            c3.metric("Desempeño / EXP", f"{categoria_egel} (+{xp_ganada} EXP)")

            st.markdown("### 🔍 Resumen de Retroalimentación")
            for i in range(total):
                f = q_df.iloc[i]; r = st.session_state.respuestas_usuario.get(i, "N/A")
                with st.container(border=True):
                    st.markdown(f"**Reactivo {i+1}** — {'✅ Correcta' if r[0] == f['respuesta_correcta'] else '❌ Incorrecta'}")
                    st.write(f"*Pregunta:* {f['pregunta']}"); st.write(f"👉 **Tu selección:** {r}")
                    if r[0] != f['respuesta_correcta']: st.write(f"🎯 **Respuesta correcta:** {f['opcion_'+f['respuesta_correcta'].lower()]}")
                    st.caption(f"💡 **Justificación:** {f['justificacion_egerina']}")

            if st.button("🔄 Volver al Menú Principal", type="primary"):
                st.session_state.caso_activo = None; st.session_state.indice_pregunta = 0; st.session_state.respuestas_usuario = {}
                st.session_state.caso_guardado_db = False; st.session_state.pregunta_revisada = False; st.rerun()
