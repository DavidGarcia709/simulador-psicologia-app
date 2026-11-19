import streamlit as st
from supabase import create_client, Client

@st.cache_resource
def init_supabase() -> Client:
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    return create_client(url, key)

supabase = init_supabase()

def registrar_usuario(email: str, password: str, username: str):
    try:
        res = supabase.auth.sign_up({"email": email, "password": password})
        if res.user:
            supabase.table("usuarios").insert({
                "id": res.user.id,
                "username": username,
                "nivel": 1,
                "xp_total": 0,
                "psicopesos": 50,
                "flashcards": [],
                "estado_examenes": {},
                "progreso_minijuegos": {"dictamen": [], "caos": []}
            }).execute()
            return True, "Registro exitoso. Ya puedes iniciar sesión."
        return False, "No se pudo completar el registro."
    except Exception as e:
        return False, str(e)

def iniciar_sesion(email: str, password: str):
    try:
        res = supabase.auth.sign_in_with_password({"email": email, "password": password})
        if res.user:
            consulta = supabase.table("usuarios").select("*").eq("id", res.user.id).execute()
            if consulta.data and len(consulta.data) > 0:
                return True, res.user, consulta.data[0]
            
            # Si el usuario existe en Auth pero no tiene fila en 'usuarios', la creamos al vuelo
            nuevo_perfil = {
                "id": res.user.id,
                "username": email.split("@")[0],
                "nivel": 1,
                "xp_total": 0,
                "psicopesos": 50,
                "flashcards": [],
                "estado_examenes": {}
            }
            insertado = supabase.table("usuarios").insert(nuevo_perfil).execute()
            datos_finales = insertado.data[0] if insertado.data else nuevo_perfil
            return True, res.user, datos_finales
        return False, None, "Credenciales inválidas."
    except Exception as e:
        return False, None, str(e)

def guardar_progreso_caso(user_id: str, caso_id: int, aciertos: int, total_preguntas: int, tiempo_segundos: int, xp_ganada: int):
    try:
        supabase.table("progreso_casos").insert({
            "user_id": user_id, "caso_id": caso_id, "aciertos": aciertos, 
            "total_preguntas": total_preguntas, "tiempo_segundos": tiempo_segundos
        }).execute()

        perfil = supabase.table("usuarios").select("xp_total", "nivel").eq("id", user_id).single().execute()
        nuevo_xp = perfil.data["xp_total"] + xp_ganada
        nuevo_nivel = max(1, nuevo_xp // 500 + 1)

        supabase.table("usuarios").update({"xp_total": nuevo_xp, "nivel": nuevo_nivel}).eq("id", user_id).execute()
        return True
    except Exception as e:
        return False

def obtener_progreso_usuario(user_id: str):
    try:
        res = supabase.table("progreso_casos").select("*").eq("user_id", user_id).execute()
        return res.data
    except: return []

def obtener_emblemas_usuario(user_id: str):
    try:
        res = supabase.table("emblemas_desbloqueados").select("catalogo_emblemas(icono, nombre)").eq("user_id", user_id).execute()
        emblemas = [item["catalogo_emblemas"]["icono"] + " " + item["catalogo_emblemas"]["nombre"] for item in res.data]
        return emblemas if emblemas else ["Aún no tienes emblemas"]
    except: return ["Error al cargar emblemas"]

# --- FUNCIONES DE PERSISTENCIA EN LA NUBE ---
def actualizar_economia_bd(user_id: str, psicopesos: int):
    try: supabase.table("usuarios").update({"psicopesos": psicopesos}).eq("id", user_id).execute()
    except: pass

def guardar_estado_examen_bd(user_id: str, estado_dict: dict):
    try: supabase.table("usuarios").update({"estado_examenes": estado_dict}).eq("id", user_id).execute()
    except: pass

def guardar_flashcards_bd(user_id: str, flashcards: list):
    try: supabase.table("usuarios").update({"flashcards": flashcards}).eq("id", user_id).execute()
    except: pass

def guardar_progreso_minijuegos_bd(user_id: str, progreso_dict: dict):
    try: supabase.table("usuarios").update({"progreso_minijuegos": progreso_dict}).eq("id", user_id).execute()
    except: pass
