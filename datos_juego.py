# datos_juego.py

TODAS_LAS_FLASHCARDS = [
    {"id": "F1", "front": "WAIS-IV / WISC-IV", "back": "Capacidad intelectual (CIT), Razonamiento Perceptual, Memoria de Trabajo"},
    {"id": "F2", "front": "Test de Bender", "back": "Maduración visomotora, rotaciones > 45° y daño orgánico"},
    {"id": "F3", "front": "MMPI-2", "back": "Escalas de Validez L (Mentira), F (Simulación) y K (Defensividad)"},
    {"id": "F4", "front": "TDAH", "back": "Síntomas antes de los 12 años en múltiples contextos (casa, escuela)"},
    {"id": "F5", "front": "Distimia", "back": "Ánimo deprimido crónico casi a diario por al menos 2 años"},
    {"id": "F6", "front": "Trastorno Límite (TLP)", "back": "Terror al abandono, impulsividad, escisión y conductas autolesivas"},
    {"id": "F7", "front": "TCC (Cognitivo-Conductual)", "back": "Reestructuración cognitiva y desensibilización sistemática"},
    {"id": "F8", "front": "Test de Cleaver", "back": "Empuje (D), Influencia (I), Constancia (S), Apego (C) en entorno laboral"},
    {"id": "F9", "front": "T-Student", "back": "Compara la diferencia de medias entre exactamente 2 grupos"},
    {"id": "F10", "front": "ANOVA", "back": "Compara la diferencia de medias entre 3 o más grupos"},
    {"id": "F11", "front": "Entrevista Semiestructurada", "back": "Tiene temas definidos a explorar, pero es flexible y sin redacción exacta"},
    {"id": "F12", "front": "Kappa de Cohen", "back": "Mide la confiabilidad interjueces (nivel de acuerdo entre dos evaluadores)"},
    {"id": "F13", "front": "RIAS, Shipley-2 y Beta-4", "back": "El EGEL evalúa su pertinencia de uso, NO la interpretación de sus datos"},
    {"id": "F14", "front": "Entrevista Estructurada", "back": "Uso de un guion directivo y rígido donde a todos se les hacen las mismas preguntas"},
    {"id": "F15", "front": "Test de Apercepción Infantil (CAT)", "back": "Usa figuras de animales o humanas para evaluar fantasías y problemas específicos"},
    {"id": "F16", "front": "Test de Illinois", "back": "Habilidades psicolingüísticas; se evalúa su pertinencia de uso, no sus datos"},
    {"id": "F17", "front": "Test de Atención D2", "back": "Se interpretan sus puntuaciones en forma de percentiles de velocidad y precisión"},
    {"id": "F18", "front": "Entrevista No Estructurada", "back": "Indagación abierta sin guion previo, donde el entrevistado marca libremente el ritmo y los tópicos del diálogo"},
]

CASOS_CLINICOS = {
    1: {
        "titulo": "Caso Clínico 1",
        "area": "Área 1: Evaluación Psicológica",
        "texto": """**I. Ficha de Identificación y Motivo de Consulta**
* **Nombre:** Javier R. | **Edad:** 34 años.
* **Ocupación:** Ingeniero de Software (Arquitecto de bases de datos).
* **Derivación:** Remitido con carácter de urgencia por psiquiatría.
* **Motivo de Consulta (Textual):** *"El psiquiatra me dijo que necesito terapia urgente porque mis pastillas ya no son suficientes. Llevo semanas sin dormir más de dos horas seguidas. Siento que mi cerebro es un motor que no se puede apagar; si no reviso el código de mi trabajo una y otra vez, estoy convencido de que los servidores del banco colapsarán, millones de personas perderán su dinero y yo iré a la cárcel. Sé que suena exagerado, pero la angustia me está destruyendo físicamente"*.

**II. Historia del Padecimiento Actual**
El cuadro comenzó hace dos años y se exacerbó dramáticamente tras su divorcio hace 8 meses. Relata intrusión constante de imágenes mentales catastróficas y pensamientos que él reconoce como irracionales, pero no puede detener.
Para neutralizar la ansiedad, desarrolló rituales de comprobación. Inicialmente revisaba su trabajo dos veces. En el último mes, escaló a niveles incapacitantes: se queda hasta las 3:00 a.m. revisando línea por línea, contando en múltiplos de cuatro. Si pierde la cuenta o lo interrumpen, siente opresión en el pecho y reinicia desde cero. Esto consume entre 5 y 6 horas de su día.
Ha perdido 8 kilos por falta de apetito (hiporexia). Manifiesta profunda desesperanza, ideación pasiva de muerte, llanto inmotivado y abulia.

**III. Evaluaciones Médicas e Interconsulta**
Acudió a urgencias dos veces creyendo sufrir infartos (taquicardia, disnea, sudoración y terror a morir inminente). Descartada patología cardiovascular, psiquiatría prescribió un ISRS y benzodiacepina, solicitando batería psicométrica para clarificar personalidad y riesgo suicida.

**IV. Historia Personal, Rasgos y Contexto Familiar**
Madre con ansiedad generalizada no tratada; padre militar punitivo. Históricamente muestra devoción excesiva por la productividad y es inflexible moralmente, siendo incapaz de delegar porque *"nadie lo hará tan perfecto como él"*. A diferencia de los rituales actuales (que lo hacen sufrir), este perfeccionismo histórico siempre lo consideró una virtud, siendo la causa de su divorcio. Vive solo y aislado.

**V. Examen Mental Inicial y Dilema Ético**
Descuido en aliño personal, evita tocar pomos de puertas. Discurso prolijo; utiliza vocabulario técnico para racionalizar sus emociones. Afecto restringido y depresivo.
* **Dilema Ético:** Recursos Humanos contacta al terapeuta exigiendo su "diagnóstico exacto" para decidir si le retiran credenciales de seguridad informática."""
    },
    2: {
        "titulo": "Caso Clínico 2",
        "area": "Área 1: Evaluación Psicológica",
        "texto": """**I. Ficha de Identificación y Motivo de Consulta**
* **Nombre:** Adriana M. | **Edad:** 9 años y 4 meses.
* **Motivo de Consulta:** Derivada por la escuela por severo rezago en lectura. Confunde letras con orientación espacial similar (b/d, p/q), lectura silábica y conductas disruptivas de escape durante el dictado (romper hojas, salir al baño).

**II. Historia del Desarrollo y Dinámica Familiar**
Marcha normativa a los 12 meses; ligero retraso de lenguaje a los 3 años (corregido). Antecedente familiar: tío paterno con dificultades lectoras. Padres en litigio judicial conflictivo por la custodia de la menor.

**III. Batería Psicométrica Aplicada**
* **WISC-IV:** ICV = 108; IRP = 102; IMT = 78; IVP = 80; CI Total (CIT) = 95 (Promedio).
* **Test de Bender (Koppitz):** Edad maduracional de 6 años y 5 meses. Errores de rotación > 45° e integración inmadura.
* **BANETA:** Percentil < 10 en procesamiento fonológico y discriminación grafema-fonema.
* **Exámenes:** Agudeza visual y audiometría normales.

**IV. Observación Conductual y Dilema Ético**
Socialización preservada; excelente exposición oral. En lectoescritura muestra inquietud motora y verbaliza *"soy la más tonta"*.
* **Dilema Ético:** El padre exige al psicólogo alterar el informe para dictaminar que el rezago es culpa exclusiva de la negligencia materna, buscando anexarlo como prueba en el juicio."""
    },
    3: {
        "titulo": "Caso Clínico 3",
        "area": "Área 2: Intervención Psicológica",
        "texto": """**I. Ficha de Identificación y Motivo de Consulta**
* **Nombre:** Sofía T. | **Edad:** 22 años | **Ocupación:** Estudiante (baja temporal).
* **Motivo:** *"Hace medio año me dio un infarto en el metro; el corazón se me salía, me ahogaba y sentí que moría. Vivo aterrada de que me vuelva a pasar"*.

**II. Historia del Padecimiento y Patrones Conductuales**
Estado de alerta e hipervigilancia ante cualquier sensación física. Interpreta cambios cardíacos pensando: *"Me va a dar un infarto y nadie me ayudará"*, detonando sudoración y sensación de que el entorno es irreal.
Huye inmediatamente de multitudes; al volver a su cuarto el terror desaparece en segundos, cristalizando la evitación. Desarrolló conductas de seguridad: lleva ansiolíticos, agua y el celular con el 911 en pantalla. Evaluaciones cardiológicas resultaron negativas.

**III. Plan de Intervención Estructurado**
* **Fase 1:** Entrenamiento riguroso en respiración lenta hacia la zona abdominal para activar vías nerviosas que frenan la taquicardia.
* **Fase 2:** Cuestionamiento lógico guiado para que descubra fallas en su razonamiento (pasar de *"es un infarto"* a *"es falsa alarma"*).
* **Fase 3:** Se le hace respirar por un popote en consulta para provocar mareo intencional y que tolere la sensación sin huir. Posteriormente se expone a la calle jerárquicamente.

**IV. Barreras Familiares**
La madre llora y sabotea las salidas sola de Sofía. El clínico descubre que tras el abandono del padre, la madre usa el miedo de la hija para mantenerla dependiente y no quedarse sola en casa."""
    },
    4: {
        "titulo": "Caso Clínico 4",
        "area": "Área 2: Intervención Psicológica",
        "texto": """**I. Ficha de Identificación y Motivo de Consulta**
* **Nombre:** Ernesto M. | **Edad:** 34 años.
* **Motivo:** *"Siempre tropiezo con la misma piedra; cuando estoy a punto de consolidar un ascenso o una relación, hago algo absurdo para arruinarlo"*.

**II. Historia Dinámica y Vínculos**
Previo a firmar su dirección operativa, llegó tarde y fue hostil con sus superiores, provocando el despido. Narra eventos dolorosos fríamente, aislando el afecto con teorías filosóficas.
Padre descalificador (*"nunca estarás a la altura"*); madre sumisa que lo usó como confidente contra el esposo. Siente inconscientemente que superar a su padre es una traición.

**III. Encuadre y Proceso Analítico**
Reglas fijas (2 sesiones semanales). Se le instruye a verbalizar sin censura todo lo que venga a su mente. El terapeuta mantiene una escucha neutral no directiva.
Ernesto relata un sueño: un hombre sin rostro de traje negro derriba una torre de cajas que él construyó. Analizan que el hombre de traje fusiona a su jefe actual y a su padre.

**IV. Evolución Transferencial**
Al sexto mes, ataca al terapeuta acusándolo de *"arrogante que busca humillarlo"*. El clínico no se defiende; controla sus emociones y le señala cómo está repitiendo en el consultorio la misma sumisión y hostilidad de su infancia. Esto provoca un impacto profundo en Ernesto, permitiéndole asimilar lógicamente el origen de su autosabotaje."""
    },
    5: {
        "titulo": "Caso Clínico 5",
        "area": "Área 2: Intervención Psicológica",
        "texto": """**I. Ficha de Identificación del Sistema**
* **Integrantes:** Roberto (Padre, 45), Carmen (Madre, 42), Santiago (Hijo, 14).
* **Motivo:** *"Santiago está insoportable, contesta a maestros y reprobó. Es el único problema que tenemos en la familia"*.

**II. Pautas de Interacción y Dinámica Actual**
Secuencia repetitiva: Padre reprende $\\rightarrow$ Madre desautoriza y minimiza falta del hijo $\\rightarrow$ Padre se enoja y aísla $\\rightarrow$ Hijo reincide.
Padres con distanciamiento íntimo severo de 2 años al borde de la separación. Cada vez que la tensión matrimonial amenaza con divorcio, el hijo comete una falta escolar grave, obligando a los padres a unirse temporalmente para resolverlo. La frontera de privacidad madre-hijo es inexistente, mientras la del padre es rígida y periférica. En la sesión 2 se usó una gráfica transgeneracional para mapear la historia familiar.

**III. Técnicas Aplicadas**
* Se les obliga a discutir en vivo la hora de llegada del hijo (*"háblenlo entre ustedes ahora mismo"*).
* El terapeuta interviene físicamente: bloquea a la madre y exige al padre acercarse para negociar la regla en equipo.
* Intervención verbal: *"Santiago no es rebelde; está sacrificando su éxito para mantenerlos ocupados y evitar su divorcio"*.
Al ceder el síntoma del hijo, la verdadera crisis conyugal emerge y los padres continúan solos el tratamiento."""
    },
    6: {
        "titulo": "Caso de Investigación 1",
        "area": "Área 3: Investigación y Medición",
        "texto": """**I. Planteamiento y Diseño del Estudio**
Evaluación de eficacia de un programa intensivo de Mindfulness sobre desgaste profesional (burnout) y reactividad fisiológica al estrés. Muestra de 60 enfermeros de urgencias con burnout clínico. Asignación mediante software aleatorio: 30 al grupo de intervención (8 semanas) y 30 a lista de espera. Se garantizó el anonimato.

**II. Adaptación Psicométrica**
Se sometió el Inventario de Maslach (MBI) traducido a un panel de 7 expertos, quienes calificaron numéricamente si cada ítem medía desgaste en el contexto mexicano, logrando un índice de concordancia de **0.91**. En prueba piloto (n=200), la evaluación de consistencia interna arrojó un índice de **0.86**.

**III. Análisis de Datos y Anomalías**
Mediciones pretest (semana 1) y postest (semana 8). Se midió la concentración de cortisol salival (µg/dL) con un cero absoluto empírico. Al correr la prueba de bondad de ajuste de Kolmogorov-Smirnov, los datos del cortisol del grupo control **no siguieron una distribución normal de campana** y presentaron varianzas desiguales.
Ignorando este fallo en los supuestos, los autores aplicaron una T de Student para muestras independientes, concluyendo una disminución del estrés catalogada como "estadísticamente significativa" con un valor **p = 0.04**.

**IV. Dilema en la Publicación**
Al redactar el artículo, el director del hospital obligó a los autores a eliminar del registro a 5 participantes que abandonaron el programa por carga laboral, obligando a recalcular los datos solo con los 25 casos de éxito para inflar la efectividad real."""
    },
    7: {
        "titulo": "Caso de Investigación 2",
        "area": "Área 3: Investigación y Medición",
        "texto": """**I. Contexto y Muestreo del Estudio**
Estudio epidemiológico para evaluar la asociación entre tiempo diario en redes sociales y rendimiento cognitivo en alumnos de bachillerato. Mediciones en un único punto temporal, sin manipulación de variables.
De un padrón de 3,200 alumnos, se dividió a la población en estratos por semestre (1°, 3° y 5°) seleccionando al azar de forma proporcional hasta lograr una muestra de 850 alumnos. Se recabó consentimiento de padres y asentimiento de los menores (16 y 17 años).

**II. Mediciones y Distribución de Datos**
Los alumnos subestimaron sus horas de uso reportadas en el cuestionario para no ser juzgados negativamente por los encuestadores. 
El examen de razonamiento abstracto mostró una distribución de frecuencias con asimetría negativa (sesgo hacia la izquierda). Un alumno brillante obtuvo una puntuación estándar Z = +2.0 (escala con Media=50, DE=10).

**III. Análisis Inferencial**
Cumpliendo normalidad, se corrió la prueba de asociación lineal obteniendo **r = -0.62** (p < 0.001), con una varianza explicada equivalente a **0.384**.
Se dividió a los alumnos en 3 grupos (Bajo, Medio, Alto uso de pantallas). Para comparar sus medias de rendimiento se corrió la prueba paramétrica correspondiente obteniendo **F = 6.45** (p = 0.002). Se buscó también predecir el puntaje futuro usando simultáneamente horas de pantalla y horas de sueño nocturno mediante un modelo matemático multivariado."""
    },
    8: {
        "titulo": "Caso de Investigación 3",
        "area": "Área 3: Investigación y Medición",
        "texto": """**I. Marco Epistemológico y Participantes**
Estudio diseñado para explorar el significado subjetivo de la pérdida en personas que sufrieron duelo de un familiar por Covid-19 sin rituales presenciales de despedida, interpretando la experiencia desde la perspectiva interna de los sujetos.
Reclutaron a los primeros 3 deudos en un centro de apoyo, y estos a su vez invitaron a otros conocidos en situaciones similares (14 informantes finales). 

**II. Procedimiento de Recolección y Análisis**
Entrevistas con preguntas abiertas y guion flexible. El equipo detuvo el reclutamiento en la entrevista 14 al darse cuenta de que las nuevas narrativas ya no aportaban categorías conceptuales inéditas al análisis. Transcribieron el discurso, fragmentándolo en unidades de significado que agruparon en categorías inductivamente.

**III. Criterios de Rigor Metodológico**
1. Contrastaron los testimonios de entrevistas con notas de diario de campo y grupos focales.
2. Mostraron los borradores a 5 informantes para validar si se sentían genuinamente representados por la interpretación de los investigadores.
3. El investigador principal anotó en un cuaderno sus propios prejuicios y emociones ante el llanto de los deudos para no contaminar su interpretación.

**IV. Consideraciones Bioéticas**
El comité de ética obligó a establecer un protocolo de contención emocional en caso de reactivación traumática durante las entrevistas. Se alteraron nombres y lugares en el reporte para imposibilitar la identificación de los participantes."""
    },
    9: {
        "titulo": "Lectura Transversal 1",
        "area": "Área 4: Transversal (Comprensión Lectora)",
        "texto": """**Ensayo: La medicalización de la tristeza**

Vivimos en la era de la patologización de la vida cotidiana. Durante los últimos cincuenta años, el sistema psiquiátrico hegemónico y la industria farmacéutica han colaborado en un proceso silencioso pero implacable: convertir las variaciones normales de las emociones humanas en enfermedades susceptibles de ser medicadas. El sufrimiento, inherente a nuestra condición mortal, ha sido despojado de su sentido existencial para ser empaquetado bajo la asepsia del diagnóstico clínico.

Tomemos como ejemplo el tratamiento del duelo en los manuales internacionales recientes. Si la pérdida de un ser amado provoca un llanto prolongado, insomnio y falta de apetito por más de un número arbitrario de semanas estipulado por los comités de expertos, el doliente es etiquetado como disfuncional y candidato a un diagnóstico de depresión mayor. 

Este enfoque ignora flagrantemente que el ser humano necesita tiempo psíquico para reorganizar su mundo tras la pérdida. Como bien advierte el sociólogo Zygmunt Bauman al hablar de la "sociedad del cansancio", el imperativo de la felicidad constante nos condena a una frustración crónica. El mercado laboral actual exige individuos siempre productivos, optimistas y resilientes; no hay espacio en el engranaje económico para la lentitud que exige la tristeza. Por ello, la fluoxetina alivia los síntomas severos de inactividad; sin embargo, no resuelve el vacío existencial que los originó. La pastilla adormece el síntoma para devolver al individuo a su cadena de producción.

Afirmar esto no es negar la existencia y brutalidad de la depresión clínica grave, la cual requiere intervención urgente. Pero es crucial que, como sociedad y gremio, nos preguntemos: ¿A quién beneficia realmente categorizar cada matiz del sufrimiento humano como una anomalía química cerebral?"""
    },
    10: {
        "titulo": "Lectura Transversal 2",
        "area": "Área 4: Transversal (Lógica Matemática)",
        "texto": """**Reporte Institucional: Deserción y Salud Mental Universitaria (2024)**

El departamento de Servicios Escolares y Bienestar Estudiantil de la Universidad Central (matrícula total vigente de 1,200 alumnos) presentó el reporte oficial de fin de ciclo. Se registró una crisis académica sin precedentes: la tasa de deserción general alcanzó el 30% del alumnado total.

Al aplicar la encuesta de salida a los alumnos que abandonaron sus carreras, los datos mostraron que el 60% de este grupo de desertores señaló "sufrir crisis de ansiedad clínica recurrentes" como la causa principal para tramitar su baja. 

Al cruzar estos datos con las cifras del centro de atención psicológica interno, se identificó un patrón de búsqueda de ayuda diferencial por género: por cada hombre que agenda una sesión de terapia, hay tres mujeres que lo hacen (proporción 3:1 a favor del género femenino). En el mes crítico de marzo, la clínica documentó un total de 160 atenciones brindadas en 30 días.

El Decano de la Facultad de Ciencias Exactas, preocupado por las estadísticas, convocó a una junta y declaró ante el consejo de profesores la siguiente norma lógica: *"Está estadísticamente comprobado que si un alumno sufre ansiedad clínica severa, entonces reprobará irremediablemente el semestre"*. Acto seguido, el coordinador de carrera levantó la mano y confirmó: *"Le informo que el alumno Carlos M. acaba de reprobar el semestre en su totalidad"*, a lo que el Decano concluyó dando un golpe en la mesa: *"Ahí lo tienen. Es un hecho indiscutible que Carlos M. sufre de ansiedad clínica severa"*. 

Para mitigar la crisis a futuro, la universidad ha decidido implementar un programa piloto aleatorio de intervención en crisis con la hipótesis formal de reducir las bajas en un 50% relativo para el ciclo entrante."""
    },
    11: {
        "titulo": "Lectura Transversal 3",
        "area": "Área 4: Transversal (Comprensión Lectora)",
        "texto": """**Ensayo: La ilusión de la neutralidad algorítmica**

En la última década, los departamentos de recursos humanos han adoptado inteligencias artificiales para filtrar currículums y agilizar el reclutamiento. Quienes defienden estas herramientas argumentan que los algoritmos son objetivos, precisos y libres de los sesgos emocionales humanos. Sin embargo, esta afirmación es una falacia tecno-optimista profunda. 

Los algoritmos de aprendizaje automático son cajas negras que se entrenan utilizando inmensas bases de datos históricas. Si una empresa, influenciada por la cultura de su época, ha contratado mayoritariamente a hombres blancos para puestos directivos durante cuarenta años, la IA identificará lógicamente estos rasgos sociodemográficos como los verdaderos "predictores de éxito" para la compañía. En consecuencia, el algoritmo penalizará automáticamente los currículums de mujeres o minorías, asumiendo que carecen del perfil histórico ideal. 

Un ejemplo empírico célebre es la herramienta de contratación que Amazon tuvo que desechar en 2018. Los ingenieros descubrieron que la inteligencia artificial degradaba sistemáticamente los CV que contenían la palabra "mujer" o que hacían referencia a universidades exclusivamente femeninas.

La neutralidad matemática es un mito peligroso cuando el modelo estadístico se alimenta de una realidad social que ya está previamente fracturada. Delegar decisiones éticas a un software no elimina la discriminación de raíz, simplemente la automatiza y la invisibiliza bajo una pátina de legitimidad científica. Por tanto, es imperativo auditar estos sistemas con perspectiva sociológica antes de permitir que un código fuente decida de forma autónoma quién es apto para integrarse al mercado laboral y quién debe ser excluido."""
    },
    12: {
        "titulo": "Lectura Transversal 4",
        "area": "Área 4: Transversal (Lógica Matemática)",
        "texto": """**Reporte Analítico: Salud Mental en Población Universitaria**

El censo anual de la clínica comunitaria reporta una población total de 2,000 estudiantes atendidos en el ciclo vigente. Del total de ingresos, el 45% fue diagnosticado con Trastorno de Ansiedad Generalizada (TAG) y el 25% con un Episodio Depresivo Mayor (EDM).

Durante una auditoría, el director del centro estableció la siguiente premisa clínica ante los médicos internos: *"Si un paciente no recibe intervención terapéutica oportuna, entonces su cuadro clínico se cronificará inevitablemente"*. Al revisar expedientes, el asistente notó que el cuadro de la paciente Laura se había cronificado, y dictaminó tajantemente que Laura era la prueba empírica de que no se le dio intervención a tiempo. 

En cuanto a la distribución del presupuesto hospitalario, las reglas de la clínica estipulan que por cada $5 pesos invertidos en el departamento de psiquiatría, se deben invertir $2 pesos en el departamento de terapia cognitivo-conductual (TCC). El presupuesto mensual total que se debe repartir íntegramente entre ambos departamentos suma $140,000 pesos exactos.

Para el programa de prevención de adicciones de la próxima semana, el protocolo exige formar grupos focales de terapia. Se cuenta con un padrón exclusivo de 6 terapeutas capacitados, pero cada grupo focal solo puede ser dirigido por un equipo de exactamente 4 terapeutas trabajando de forma simultánea.

Finalmente, el registro de urgencias psiquiátricas indica una alarmante alza en las atenciones por crisis de pánico. Hace dos meses se atendieron 15 crisis; el mes pasado la cifra subió a 45, y el departamento de proyección estadística asume que el próximo mes se atenderán 135 crisis si la tendencia no se interrumpe con medidas drásticas."""
    }
}

BANCO_NARRATIVO = [
    # =================================================================
    # ÁREA 1: EVALUACIÓN PSICOLÓGICA (PSICOPATOLOGÍA Y DIAGNÓSTICO)
    # =================================================================
    {
        "area": "Evaluación Psicológica", 
        "dialogo": "«Paciente masculino presenta delirios persecutorios ('la policía me sigue') y alucinaciones auditivas de mando desde hace 3 meses. En la entrevista se observa aplanamiento afectivo. No hay consumo de sustancias.»", 
        "respuesta": "Trastorno Esquizofreniforme", 
        "distractores": ["Esquizofrenia", "Trastorno Esquizoafectivo", "Trastorno Delirante"]
    },
    {
        "area": "Evaluación Psicológica", 
        "dialogo": "«Gerente de 45 años es derivado a consulta. Refiere: 'Si mi escritorio no está perfectamente simétrico y mis subordinados no siguen mis listas al pie de la letra, son unos mediocres'. Muestra excesiva devoción al trabajo.»", 
        "respuesta": "Trastorno de la Personalidad Obsesivo-Compulsiva", 
        "distractores": ["Trastorno Obsesivo-Compulsivo (TOC)", "Trastorno de la Personalidad Narcisista", "Trastorno de Ansiedad Generalizada"]
    },
    {
        "area": "Evaluación Psicológica", 
        "dialogo": "«Paciente sobrevivió a un accidente automovilístico grave hace 3 meses. Hoy reporta pesadillas recurrentes (reexperimentación del miedo), anhedonia, alteraciones del sueño y se niega a subir a cualquier vehículo.»", 
        "respuesta": "Trastorno de Estrés Postraumático (TEPT)", 
        "distractores": ["Trastorno de Adaptación (Agudo)", "Trastorno de Ansiedad por Separación", "Trastorno de Pánico"]
    },
    {
        "area": "Evaluación Psicológica", 
        "dialogo": "«Mido 1.65m y peso 68kg. Una vez a la semana compro comida a escondidas y como hasta sentir dolor. Luego siento culpa extrema y me provoco el vómito. Llevo 4 meses así.»", 
        "respuesta": "Bulimia Nerviosa", 
        "distractores": ["Trastorno por Atracón", "Anorexia Nerviosa (Tipo Purgativo)", "Trastorno de Evitación de la Ingestión"]
    },
    {
        "area": "Evaluación Psicológica", 
        "dialogo": "«Llevo una semana completa sin dormir y me siento lleno de energía. Mi mente va a mil por hora, he gastado mis ahorros y siento que tengo la capacidad de leerle la mente a la gente.»", 
        "respuesta": "Trastorno Bipolar Tipo I (Episodio Maníaco)", 
        "distractores": ["Trastorno Bipolar Tipo II (Hipomanía)", "Trastorno Ciclotímico", "Trastorno Depresivo Mayor con síntomas psicóticos"]
    },
    {
        "area": "Evaluación Psicológica", 
        "dialogo": "«Mi abuelo de 81 años empezó a olvidar dónde deja las cosas desde que enviudó hace 2 meses. Llora mucho, come poco, está postrado y dice que su cabeza ya no sirve.»", 
        "respuesta": "Pseudodemencia Depresiva", 
        "distractores": ["Trastorno Neurocognitivo Mayor (Alzheimer)", "Delirium", "Trastorno de Ansiedad Generalizada"]
    },
    {
        "area": "Evaluación Psicológica", 
        "dialogo": "«No puedo ir al cine ni subir al metro. Si estoy ahí y me da un ataque de pánico, será imposible escapar o pedir ayuda. Llevo meses sin poder salir de mi casa solo.»", 
        "respuesta": "Agorafobia", 
        "distractores": ["Trastorno de Ansiedad Social", "Trastorno de Pánico", "Fobia Específica (Claustrofobia)"]
    },
    {
        "area": "Evaluación Psicológica", 
        "dialogo": "«Nadie en esta empresa está a mi nivel intelectual. Merezco un trato especial y si tengo que humillar o manipular a los demás para ascender, es su problema por ser mediocres.»", 
        "respuesta": "Trastorno de la Personalidad Narcisista", 
        "distractores": ["Trastorno de la Personalidad Antisocial", "Trastorno Histriónico de la Personalidad", "Trastorno Paranoide de la Personalidad"]
    },
    {
        "area": "Evaluación Psicológica", 
        "dialogo": "«Escolar de 4 años, con vocabulario pedante. Carece de reciprocidad socioemocional, no hace contacto visual, aletea las manos y hace rabietas coléricas si cambian la ruta a la escuela.»", 
        "respuesta": "Trastorno del Espectro Autista (TEA)", 
        "distractores": ["Trastorno de la Comunicación Social", "TDAH", "Trastorno de Integración Sensorial"]
    },

    # =================================================================
    # ÁREA 1: EVALUACIÓN PSICOLÓGICA (INSTRUMENTOS Y PSICOMETRÍA)
    # =================================================================
    {
        "area": "Evaluación Psicológica", 
        "dialogo": "«[Reporte Médico-Legal] Tras un choque leve a 10 km/h, el paciente exige indemnización alegando ceguera repentina. El examen neurológico es limpio. En el MMPI-2, la escala F (Infrecuencia) arroja T > 110.»", 
        "respuesta": "Simulación (Fingimiento clínico)", 
        "distractores": ["Trastorno de Síntomas Somáticos", "Trastorno Facticio", "Trastorno de Conversión"]
    },
    {
        "area": "Evaluación Psicológica", 
        "dialogo": "«[Perfil Psicométrico] El sujeto presenta una elevación severa (Puntuación T > 75) en las escalas 4 (Desviación Psicopática) y 9 (Hipomanía) del MMPI-2, con la escala L baja.»", 
        "respuesta": "Perfil Impulsivo / Actuador", 
        "distractores": ["Perfil Depresivo / Ansioso", "Perfil de Fingimiento / Simulación", "Perfil Psicótico"]
    },
    {
        "area": "Evaluación Psicológica", 
        "dialogo": "«[Protocolo] El escolar de 8 años dibuja los puntos como círculos rellenados, no cierra las figuras y rota la tarjeta A en 90 grados exactos. Presenta rezago en lectura y escritura.»", 
        "respuesta": "Test de Bender (Indicadores de organicidad / Koppitz)", 
        "distractores": ["WISC-IV (Índice de Razonamiento Perceptual)", "Test de la Figura Humana (Machover)", "Test de Matrices de Raven"]
    },
    {
        "area": "Evaluación Psicológica", 
        "dialogo": "«Paciente de 10 años de comunidad indígena remota con dominio limitado del español. Se requiere evaluar el Factor G de inteligencia libre de sesgo cultural y verbal.»", 
        "respuesta": "Test de Matrices Progresivas de Raven", 
        "distractores": ["WISC-IV", "Test de Dominós (D-48)", "Batería BANETA"]
    },
    {
        "area": "Evaluación Psicológica", 
        "dialogo": "«[Resultados WISC-IV] Obtuvo Índice de Comprensión Verbal de 115, pero Memoria de Trabajo de 75 y Velocidad de Procesamiento de 80. Falla sistemáticamente en retención a corto plazo.»", 
        "respuesta": "Trastorno del Aprendizaje (Discrepancia de Índices)", 
        "distractores": ["Discapacidad Intelectual Leve", "Trastorno por Déficit de Atención", "Capacidad Intelectual Limítrofe"]
    },
    {
        "area": "Evaluación Psicológica", 
        "dialogo": "«Se requiere evaluar de forma complementaria la percepción del esquema corporal, la autoimagen y posibles dinámicas de violencia intrafamiliar en un niño de 7 años.»", 
        "respuesta": "Test de la Figura Humana (Machover) / H-T-P", 
        "distractores": ["Test de Apercepción Temática (TAT)", "Test de Cleaver", "16 PF de Cattell"]
    },
    {
        "area": "Evaluación Psicológica", 
        "dialogo": "«Ejecutivo de 29 años acude por agotamiento laboral. El clínico lleva una lista de áreas obligatorias por explorar (sueño, consumo de café, carga horaria), pero adapta el orden y agrega preguntas según lo que el paciente relata.»", 
        "respuesta": "Entrevista Semiestructurada", 
        "distractores": ["Entrevista Directiva Estructurada", "Entrevista No Estructurada", "Asociación Libre (Psicoanálisis)"]
    },
    {
        "area": "Evaluación Psicológica", 
        "dialogo": "«Adolescente de 16 años requiere una evaluación rápida de inteligencia general por motivos vocacionales. El psicólogo necesita una prueba breve que NO requiera interpretar subescalas complejas.»", 
        "respuesta": "Escala Shipley-2 (o Beta-4)", 
        "distractores": ["WAIS-IV (Perfil Completo)", "Test de Apercepción Temática (TAT)", "WISC-IV (Índices Estructurales)"]
    },
    {
        "area": "Evaluación Psicológica", 
        "dialogo": "«Niña de 10 años canalizada por inversión persistente de figuras geométricas, desorganización espacial en cuadernos y sospecha de asimetría cognitiva. Se requiere evaluar perfil intelectual y madurez visomotora.»", 
        "respuesta": "WISC-IV y Test de Bender", 
        "distractores": ["Rorschach y Test de la Figura Humana", "Frases incompletas de Sacks y Persona bajo la lluvia", "WAIS-IV y Test de Dominós D-48"]
    },
    {
        "area": "Evaluación Psicológica", 
        "dialogo": "«En el dibujo de la Figura Humana (Machover), el paciente dibuja un monstruo grotesco con manos excesivamente grandes, trazos vigorosos y un sombreado intenso en el rostro.»", 
        "respuesta": "Signos cualitativos de agresividad", 
        "distractores": ["Indicadores de alta inteligencia fluida", "Mecanismo de sublimación adaptativa", "Perfil de organicidad motora pura"]
    },
    {
        "area": "Evaluación Psicológica", 
        "dialogo": "«Profesor jubilado de 74 años es llevado por su hija: repite las mismas preguntas en lapsos de diez minutos y se desorientó al volver del mercado. Se busca una evaluación breve inicial antes de aplicar pruebas neuropsicológicas extensas.»", 
        "respuesta": "Escalas de tamizaje (ej. Mini-Mental / MoCA)", 
        "distractores": ["MMPI-2-RF", "Inventario BATTELLE", "Test de Illinois de Habilidades Psicolingüísticas"]
    },

    # =================================================================
    # ÁREA 2: INTERVENCIÓN PSICOLÓGICA
    # =================================================================
    {
        "area": "Intervención", 
        "dialogo": "«Paciente con TOC severo (lavado de manos hasta sangrar). El terapeuta le indica tocar los pomos de las puertas del consultorio y le prohíbe realizar el ritual de lavado.»", 
        "respuesta": "TCC (Exposición con Prevención de Respuesta)", 
        "distractores": ["Psicoanálisis (Análisis del trauma)", "Terapia Gestalt (Silla vacía)", "Terapia Sistémica (Reestructuración)"]
    },
    {
        "area": "Intervención", 
        "dialogo": "«Los padres no se hablan tras el divorcio; la madre le dice al hijo adolescente: 'Dile a tu padre que nos dé dinero', y el padre le responde insultos a través de él.»", 
        "respuesta": "Terapia Sistémica (Triangulación)", 
        "distractores": ["TCC (Modificación de conducta)", "Psicoanálisis (Complejo de Edipo)", "Terapia Humanista (Empatía)"]
    },
    {
        "area": "Intervención", 
        "dialogo": "«El paciente se enfurece súbitamente porque el terapeuta miró el reloj: '¡Eres igual de exigente e insensible que mi jefe y mi padre, a nadie le importo!'.»", 
        "respuesta": "Psicoanálisis (Análisis de la Transferencia)", 
        "distractores": ["TCC (Control de la ira)", "Terapia Breve Centrada en Soluciones", "Terapia de Aceptación y Compromiso"]
    },
    {
        "area": "Intervención", 
        "dialogo": "«'Si repruebo este examen de titulación, significa que soy un fracaso absoluto en la vida y nunca lograré nada'. El terapeuta busca debatir esta evidencia.»", 
        "respuesta": "TCC (Reestructuración de Distorsiones Cognitivas)", 
        "distractores": ["Terapia Existencial", "Psicoanálisis (Catarsis)", "Terapia Narrativa"]
    },
    {
        "area": "Intervención", 
        "dialogo": "«Familia con hija adolescente con insomnio por ansiedad. El terapeuta instruye: 'Esta semana te prohíbo dormir; debes quedarte despierta toda la noche vigilando la casa'.»", 
        "respuesta": "Terapia Sistémica (Intervención Paradójica)", 
        "distractores": ["TCC (Higiene del sueño)", "Terapia Gestalt (Darse cuenta)", "Psicoanálisis (Interpretación)"]
    },
    {
        "area": "Intervención", 
        "dialogo": "«El paciente describe con voz monótona cómo su esposa lo abandonó, pero está apretando fuertemente los puños. El clínico le pide que preste atención a sus manos en este momento.»", 
        "respuesta": "Terapia Gestalt (Fomento del 'Darse cuenta' / Aquí y Ahora)", 
        "distractores": ["Psicoanálisis (Asociación Libre)", "TCC (Relajación Muscular)", "Terapia Centrada en el Cliente"]
    },
    {
        "area": "Intervención", 
        "dialogo": "«Paciente con Trastorno Límite de la Personalidad (TLP) presenta desregulación emocional severa, escisión e ideación suicida crónica. Requiere entrenamiento en tolerancia al malestar.»", 
        "respuesta": "Terapia Dialéctica Conductual (DBT)", 
        "distractores": ["Psicoanálisis Clásico", "Terapia Familiar Estructural", "Terapia Racional Emotiva (TREC)"]
    },
    {
        "area": "Intervención", 
        "dialogo": "«Niño con ira incontrolable. El terapeuta instruye: 'Vamos a dibujar al Monstruo del Enojo. ¿Qué te susurra el Monstruo al oído para que pierdas el control?'.»", 
        "respuesta": "Terapia Narrativa (Externalización del Síntoma)", 
        "distractores": ["TCC (Economía de fichas)", "Terapia Gestalt (Role-play)", "Psicoanálisis (Terapia de juego)"]
    },
    {
        "area": "Intervención", 
        "dialogo": "«El terapeuta pregunta en la primera sesión: 'Imagina que esta noche ocurre un milagro y tu problema desaparece. Al despertar, ¿cuál sería la primera señal del milagro?'.»", 
        "respuesta": "Terapia Breve Centrada en Soluciones (Pregunta Milagro)", 
        "distractores": ["TCC (Ensayo conductual)", "Logoterapia (Sentido de Vida)", "Terapia Sistémica (Excepción)"]
    },
    {
        "area": "Intervención", 
        "dialogo": "«La madre lee el diario de su hija de 16 años, suelen vestir de forma idéntica y la madre utiliza frases como: 'Nosotras estamos en la preparatoria y nos duele la cabeza'.»", 
        "respuesta": "Terapia Sistémica (Límites Difusos / Familia Aglutinada)", 
        "distractores": ["Psicoanálisis (Simbiosis)", "TCC (Entrenamiento Asertivo)", "Gestalt (Confluencia)"]
    },
    {
        "area": "Intervención", 
        "dialogo": "«Paciente con fobia a volar. El terapeuta enseña relajación muscular progresiva y luego lo hace imaginar que compra un boleto, subiendo la ansiedad gradualmente en una jerarquía.»", 
        "respuesta": "TCC (Desensibilización Sistemática)", 
        "distractores": ["EMDR", "Terapia de Aceptación y Compromiso", "Psicoanálisis (Análisis de evitación)"]
    },
    {
        "area": "Intervención", 
        "dialogo": "«'Siento que soy horrible, nadie me quiere'. El terapeuta responde: 'Sientes un peso inmenso y doloroso sobre ti en este momento, estoy aquí contigo y te acepto'.»", 
        "respuesta": "Terapia Humanista (Empatía y Aceptación Incondicional)", 
        "distractores": ["TCC (Validación cognitiva)", "Psicoanálisis (Contratransferencia)", "Terapia Racional Emotiva (TREC)"]
    },
    {
        "area": "Intervención", 
        "dialogo": "«El paciente lleva un mes cancelando sesiones de último minuto o cambiando abruptamente de tema de conversación cada vez que se menciona a su hermano fallecido.»", 
        "respuesta": "Psicoanálisis (Análisis de la Resistencia)", 
        "distractores": ["TCC (Falta de adherencia)", "Terapia Breve (Falta de motivación)", "Terapia Sistémica (Homeostasis)"]
    },
    {
        "area": "Intervención", 
        "dialogo": "«Un hombre lidera campañas públicas agresivas contra la homosexualidad, mientras secretamente lucha con impulsos homosexuales inaceptables para su propia moral.»", 
        "respuesta": "Psicoanálisis (Mecanismo de Formación Reactiva)", 
        "distractores": ["TCC (Disonancia Cognitiva)", "Terapia Gestalt (Proyección)", "Terapia Existencial (Negación)"]
    },
    {
        "area": "Intervención", 
        "dialogo": "«Paciente con Depresión Mayor severa. No sale de la cama hace semanas. Antes de intentar cambiar sus pensamientos, el terapeuta le asigna la tarea de levantarse a tomar agua.»", 
        "respuesta": "TCC (Activación Conductual)", 
        "distractores": ["Psicoanálisis (Elaboración del duelo)", "Logoterapia (Sentido de vida)", "Terapia Sistémica (Ruptura del patrón)"]
    },

    # =================================================================
    # ÁREA 3: INVESTIGACIÓN Y MEDICIÓN
    # =================================================================
    {
        "area": "Investigación", 
        "dialogo": "«Se busca evaluar el impacto de un taller de estrés. Se miden los niveles de cortisol de 30 participantes ANTES de iniciar y a los mismos 30 AL FINALIZAR el mes de curso.»", 
        "respuesta": "T-Student para muestras relacionadas (pareadas)", 
        "distractores": ["T-Student para muestras independientes", "ANOVA de medidas repetidas", "Correlación de Pearson"]
    },
    {
        "area": "Investigación", 
        "dialogo": "«Al diseñar una escala de 'Liderazgo', el autor se asegura de incluir ítems sobre toma de decisiones, empatía y oratoria, cubriendo todas las facetas del marco teórico conceptual.»", 
        "respuesta": "Validez de Contenido", 
        "distractores": ["Validez de Criterio", "Confiabilidad Test-Retest", "Alfa de Cronbach"]
    },
    {
        "area": "Investigación", 
        "dialogo": "«Un investigador aplica una prueba de inteligencia a un grupo y, seis meses después, aplica EXACTAMENTE la misma prueba al mismo grupo para ver si los puntajes son estables en el tiempo.»", 
        "respuesta": "Confiabilidad Test-Retest", 
        "distractores": ["Confiabilidad por Mitades (Split-half)", "Validez Predictiva", "Validez de Constructo"]
    },
    {
        "area": "Investigación", 
        "dialogo": "«Se busca determinar si existe una asociación estadística pura entre el 'Nivel Socioeconómico' (Bajo/Medio/Alto) y la 'Preferencia de Tratamiento' (Psiquiátrico/Psicológico).»", 
        "respuesta": "Chi Cuadrada de Pearson", 
        "distractores": ["ANOVA de un factor", "Correlación de Spearman", "Regresión Lineal Múltiple"]
    },
    {
        "area": "Investigación", 
        "dialogo": "«El análisis estadístico revela la siguiente conclusión: 'A mayor cantidad de horas jugando videojuegos violentos, menor es el rendimiento académico en matemáticas' (r = -0.75).»", 
        "respuesta": "Correlación Negativa Fuerte", 
        "distractores": ["Causalidad Directa y Absoluta", "Correlación Positiva Fuerte", "Diferencia de Medias Significativa"]
    },
    {
        "area": "Investigación", 
        "dialogo": "«Se prueba la eficacia de una nueva terapia en un hospital. No es posible asignar pacientes al azar, por lo que se utilizan los grupos intactos ya formados (turno matutino vs vespertino).»", 
        "respuesta": "Diseño Cuasiexperimental", 
        "distractores": ["Diseño Experimental Puro", "Diseño Correlacional", "Estudio Ex Post Facto"]
    },
    {
        "area": "Investigación", 
        "dialogo": "«Para entender cómo viven el duelo las madres en pandemia, el investigador realiza entrevistas profundas buscando extraer el significado subjetivo y la esencia de su experiencia.»", 
        "respuesta": "Enfoque Fenomenológico (Cualitativo)", 
        "distractores": ["Enfoque Etnográfico", "Investigación Acción Participativa", "Estudio Correlacional Mixto"]
    },
    {
        "area": "Investigación", 
        "dialogo": "«En los salarios de una clínica, el dueño gana 500,000 al mes, y los 50 terapeutas ganan 6,000. Ante valores tan atípicos, ¿cuál es la medida de tendencia central más representativa?»", 
        "respuesta": "La Mediana", 
        "distractores": ["La Media (Promedio Matemático)", "La Moda", "La Desviación Estándar"]
    },
    {
        "area": "Investigación", 
        "dialogo": "«Se crea un test rápido de riesgo suicida de 5 preguntas y se aplican simultáneamente sus resultados con el Inventario de Beck (estándar de oro) a 100 personas para ver si correlacionan.»", 
        "respuesta": "Validez de Criterio (Concurrente)", 
        "distractores": ["Validez de Contenido", "Confiabilidad Test-Retest", "Validez Aparente"]
    },
    {
        "area": "Investigación", 
        "dialogo": "«Se evaluó a 50 niños cuando tenían 5 años, se volvió a evaluar a los mismos niños a los 10 años, y finalmente a los 15 años, para observar el desarrollo evolutivo de su juicio moral.»", 
        "respuesta": "Diseño Longitudinal", 
        "distractores": ["Diseño Transversal (Cross-sectional)", "Diseño Experimental", "Estudio de Caso Único"]
    },
    {
        "area": "Investigación", 
        "dialogo": "«Al correr la prueba de normalidad Kolmogorov-Smirnov en el peso de 100 pacientes, arrojó p=0.01. Los datos están fuertemente sesgados a la izquierda y no tienen forma de campana.»", 
        "respuesta": "Usar Pruebas No Paramétricas (ej. U de Mann-Whitney)", 
        "distractores": ["Usar forzosamente la T-Student", "Correr un ANOVA paramétrico", "Usar Correlación de Pearson"]
    },
    {
        "area": "Investigación", 
        "dialogo": "«De 5,000 estudiantes universitarios, el 60% son de ingeniería y el 40% de artes. Se seleccionan 100 estudiantes respetando meticulosamente esa misma proporción porcentual.»", 
        "respuesta": "Muestreo Estratificado Proporcional", 
        "distractores": ["Muestreo Aleatorio Simple", "Muestreo por Conveniencia", "Muestreo por Bola de Nieve"]
    },
    {
        "area": "Investigación", 
        "dialogo": "«En un experimento clínico, la diferencia en reducción de síntomas de depresión entre el grupo pastilla y el grupo placebo obtuvo un valor p = 0.02 (asumiendo un nivel alfa de 0.05).»", 
        "respuesta": "Se rechaza la Hipótesis Nula (El resultado es estadísticamente significativo)", 
        "distractores": ["Se acepta la Hipótesis Nula", "El resultado se debe completamente al azar", "El instrumento de medición no tiene validez"]
    },
    {
        "area": "Investigación", 
        "dialogo": "«[Dilema Ético] Un investigador engaña a los participantes haciéndoles creer que dan descargas mortales a otra persona, causándoles crisis de angustia y llanto real durante el proceso.»", 
        "respuesta": "Violación del principio ético de No Maleficencia", 
        "distractores": ["Violación de Confidencialidad", "Falta de Validez Ecológica", "Violación del Anonimato"]
    },
    {
        "area": "Investigación", 
        "dialogo": "«Se busca comparar si existen diferencias estadísticas reales en el nivel de 'Comprensión Lectora' (medido en un puntaje continuo de 0 a 100) entre escuelas Públicas vs escuelas Privadas.»", 
        "respuesta": "T-Student para muestras independientes", 
        "distractores": ["T-Student pareada (medidas repetidas)", "Correlación Lineal de Pearson", "Análisis Chi Cuadrada"]
    },
    {
        "area": "Investigación", 
        "dialogo": "«Dos psicólogos observan a un niño en cámara de Gesell y califican por separado la cantidad de conductas disruptivas. Quieren calcular estadísticamente qué tan de acuerdo están sus evaluaciones.»", 
        "respuesta": "Kappa de Cohen", 
        "distractores": ["Alfa de Cronbach", "T-Student para muestras independientes", "Correlación de Pearson"]
    }
]

DATOS_CAOS = {
    # ---------------------------------------------------------
    # INSTRUMENTOS Y PSICOMETRÍA
    # ---------------------------------------------------------
    "Examen Mental": {
        "area": "Evaluación Psicológica", 
        "correctos": ["Aspecto físico y conducta motora", "Forma y curso del pensamiento", "Alteraciones de la percepción", "Nivel de Insight"]
    },
    "WISC-IV (Índices)": {
        "area": "Evaluación Psicológica", 
        "correctos": ["Comprensión Verbal", "Razonamiento Perceptual", "Memoria de Trabajo", "Velocidad de Procesamiento"]
    },
    "Test Gestáltico Visomotor (Bender)": {
        "area": "Evaluación Psicológica", 
        "correctos": ["Maduración Perceptomotora", "Indicadores de organicidad (Rotaciones)", "Indicadores emocionales", "Sistema de calificación Koppitz"]
    },
    "MMPI-2 (Escalas de Validez)": {
        "area": "Evaluación Psicológica", 
        "correctos": ["Escala L (Mentira)", "Escala F (Infrecuencia)", "Escala K (Defensividad)", "Detectan simulación o resistencia"]
    },
    "Figura Humana (Machover)": {
        "area": "Evaluación Psicológica", 
        "correctos": ["Psicópatas: Manos en bolsillos / Trazos vigorosos", "Dependencia: Énfasis en botones y línea media", "Esquizofrénicos: Órganos internos visibles", "Deprimidos: Dibujos muy pequeños"]
    },
    "Batería BANETA": {
        "area": "Evaluación Psicológica", 
        "correctos": ["Conciencia fonológica", "Trastornos del aprendizaje (Dislexia)", "Atención y memoria", "Aplicable de 7 a 11 años"]
    },
    "Test de Cleaver": {
        "area": "Evaluación Psicológica", 
        "correctos": ["Empuje (D) para lograr resultados", "Influencia (I) en las personas", "Constancia (S) en el trabajo", "Apego (C) a normas y procedimientos"]
    },
    "Entrevista Clínica": {
        "area": "Evaluación Psicológica", 
        "correctos": ["Estructurada / Directiva", "Semi-estructurada (Flexible)", "No estructurada (Conversacional)", "Establecimiento del Rapport"]
    },
    "Pruebas de Inteligencia Breve": {
        "area": "Evaluación Psicológica", 
        "correctos": ["Test RIAS", "Escala Shipley-2", "Beta-4", "Se evalúa pertinencia de uso, no perfil completo"]
    },
    "Test de Apercepción Infantil (CAT)": {
        "area": "Evaluación Psicológica", 
        "correctos": ["Láminas con figuras de animales", "Láminas con figuras humanas", "Exploración de dinámicas intrapsíquicas", "Problemas escolares y familiares"]
    },
    "Test de Atención D2": {
        "area": "Evaluación Psicológica", 
        "correctos": ["Mide velocidad de procesamiento atencional", "Mide precisión y control inhibitorio", "Interpretación por percentiles normativos", "Prueba de cancelación de estímulos"]
    },

    # ---------------------------------------------------------
    # PSICOPATOLOGÍA Y DIAGNÓSTICO (DSM-5)
    # ---------------------------------------------------------
    "T. Límite de la Personalidad": {
        "area": "Evaluación Psicológica", 
        "correctos": ["Inestabilidad en relaciones (Escisión)", "Notable impulsividad", "Autoimagen inestable", "Conductas autolesivas recurrentes"]
    },
    "T. Antisocial de la Personalidad": {
        "area": "Evaluación Psicológica", 
        "correctos": ["Falta de remordimiento clínico", "Desprecio por normas", "Impulsividad agresiva", "Mayor de 18 años con antecedente de T. Disocial"]
    },
    "Trastorno Esquizofreniforme": {
        "area": "Evaluación Psicológica", 
        "correctos": ["Duración entre 1 y 6 meses", "Síntomas positivos", "Síntomas negativos", "Deterioro funcional no es indispensable"]
    },
    "TDAH": {
        "area": "Evaluación Psicológica", 
        "correctos": ["Síntomas presentes antes de los 12 años", "Afectación en dos o más contextos", "Inatención persistente", "Hiperactividad motora"]
    },
    "Trastorno Depresivo Mayor": {
        "area": "Evaluación Psicológica", 
        "correctos": ["Síntomas continuos por al menos 2 semanas", "Anhedonia absoluta", "Ideación pasiva o activa de muerte", "Insomnio severo o hipersomnia"]
    },
    "Trastornos del Aprendizaje": {
        "area": "Evaluación Psicológica", 
        "correctos": ["Dislexia (Lectura fluida y comprensión)", "Disgrafía (Expresión escrita)", "Discalculia (Razonamiento matemático)", "Inteligencia global conservada (CI promedio)"]
    },

    # ---------------------------------------------------------
    # PSICOLOGÍA ORGANIZACIONAL
    # ---------------------------------------------------------
    "Evaluación del Desempeño": {
        "area": "Evaluación Psicológica", 
        "correctos": ["Retroalimentación de 360°", "Métricas KPI", "Identificación de brechas de rendimiento", "Base para el plan de carrera profesional"]
    },
    "DNC (Detección de Necesidades de Capacitación)": {
        "area": "Evaluación Psicológica", 
        "correctos": ["Identifica brechas de competencias operativas", "Se apoya en entrevistas a supervisores", "Busca mejora del desempeño organizacional", "Deriva en un plan anual estructurado"]
    },
    "NOM-035-STPS": {
        "area": "Evaluación Psicológica", 
        "correctos": ["Identifica Factores de Riesgo Psicosocial", "Previene cargas excesivas de trabajo", "Previene el liderazgo negativo", "Promueve un entorno organizacional favorable"]
    },

    # ---------------------------------------------------------
    # INTERVENCIÓN PSICOLÓGICA
    # ---------------------------------------------------------
    "Niveles de Intervención en Salud": {
        "area": "Intervención", 
        "correctos": ["Primaria (Prevención en población sana)", "Secundaria (Detección y tratamiento temprano)", "Terciaria (Rehabilitación)", "Evitar secuelas crónicas y recaídas"]
    },
    "Terapia Cognitivo Conductual (TCC)": {
        "area": "Intervención", 
        "correctos": ["Reestructuración de pensamientos irracionales", "Exposición y prevención de respuesta (EPR)", "Desensibilización Sistemática", "Registro de conductas (Autorregistros)"]
    },
    "Psicoanálisis": {
        "area": "Intervención", 
        "correctos": ["Transferencia y Contratransferencia", "Análisis de Mecanismos de Defensa", "Inconsciente y resistencia", "Asociación Libre"]
    },
    "Terapia Humanista": {
        "area": "Intervención", 
        "correctos": ["Empatía clínica profunda", "Aceptación positiva incondicional", "Reflejo emocional", "Modelo centrado en el cliente de Rogers"]
    },
    "Terapia Gestalt": {
        "area": "Intervención", 
        "correctos": ["Fomento del Darse Cuenta (Awareness)", "Técnica de la Silla Vacía", "Focalización en el Aquí y Ahora", "Resolución de asuntos inconclusos"]
    },
    "Terapia Sistémica": {
        "area": "Intervención", 
        "correctos": ["Identificación de triangulación patológica", "Manejo de límites difusos o aglutinados", "Concepto de Paciente Identificado", "Elaboración e interpretación de Genograma"]
    },
    "Terapia Racional Emotiva Conductual (TREC)": {
        "area": "Intervención", 
        "correctos": ["Modelo teórico A-B-C", "Identificación de creencias irracionales centrales", "Técnica de disputa socrática", "Teoría desarrollada por Albert Ellis"]
    },
    "Terapia Breve Centrada en Soluciones": {
        "area": "Intervención", 
        "correctos": ["Técnica de la Pregunta Milagro", "Búsqueda activa de Excepciones", "Uso de Preguntas de Escalamiento", "Modelo originado por Steve de Shazer"]
    },
    "Terapia de Aceptación y Compromiso (ACT)": {
        "area": "Intervención", 
        "correctos": ["Promoción de la flexibilidad psicológica", "Técnicas de defusión cognitiva", "Atención plena al momento presente (Mindfulness)", "Compromiso con valores personales"]
    },
    "Terapia Dialéctica Conductual (DBT)": {
        "area": "Intervención", 
        "correctos": ["Modelo creado por Marsha Linehan", "Entrenamiento en regulación emocional", "Entrenamiento en tolerancia al malestar", "Validación clínica profunda"]
    },
    "Terapia Narrativa": {
        "area": "Intervención", 
        "correctos": ["Modelo desarrollado por Michael White", "Externalización del síntoma o problema", "Creación de historias alternativas", "Uso de testigos externos"]
    },
    "Economía de Fichas": {
        "area": "Intervención", 
        "correctos": ["Bases de Condicionamiento Operante", "Aplicación sistemática de Refuerzo positivo", "Técnica de Costo de Respuesta", "Uso de tokens intercambiables"]
    },
    "Intervención en Crisis": {
        "area": "Intervención", 
        "correctos": ["Aplicación de Primeros Auxilios Psicológicos", "Objetivo principal de restablecer equilibrio", "Activación inmediata de redes de apoyo", "Abordaje de duración focalizada y breve"]
    },

    # ---------------------------------------------------------
    # INVESTIGACIÓN, MEDICIÓN Y ESTADÍSTICA
    # ---------------------------------------------------------
    "Diseño Experimental Puro": {
        "area": "Investigación", 
        "correctos": ["Manipulación estricta de la Variable Independiente", "Asignación por Aleatorización (al azar)", "Requiere obligatoriamente un Grupo Control", "Busca establecer relaciones de causalidad directa"]
    },
    "Diseño Cuasiexperimental": {
        "area": "Investigación", 
        "correctos": ["Utiliza grupos intactos ya conformados", "Carencia de aleatorización previa", "Presenta menor validez interna que el experimento puro", "Común en contextos naturales o aulas escolares"]
    },
    "T-Student vs ANOVA": {
        "area": "Investigación", 
        "correctos": ["T-Student compara medias de exactamente 2 grupos", "ANOVA compara medias de 3 o más grupos", "Ambas requieren variables dependientes Cuantitativas", "Pruebas de Estadística Inferencial paramétrica"]
    },
    "Correlación de Pearson": {
        "area": "Investigación", 
        "correctos": ["Busca relación lineal entre datos continuos", "Requiere dos variables cuantitativas con normalidad", "Presenta un rango absoluto de -1 a +1", "Mide fuerza y dirección asociativa"]
    },
    "Chi Cuadrada de Pearson": {
        "area": "Investigación", 
        "correctos": ["Usa variables categóricas o nominales exclusivas", "Analiza diferencias de frecuencias observadas", "Es una Prueba de tipo no paramétrico", "Evalúa independencia estadística entre variables"]
    },
    "Confiabilidad Psicométrica": {
        "area": "Investigación", 
        "correctos": ["Alfa de Cronbach mide Consistencia interna", "Kappa de Cohen evalúa confiabilidad Interjueces", "Test-Retest evalúa estabilidad temporal", "Split-Half evalúa correlación por mitades"]
    },
    "Validez de Constructo": {
        "area": "Investigación", 
        "correctos": ["Uso riguroso de Análisis Factorial", "Asegura medir fielmente el concepto teórico", "Incluye el concepto de Validez Convergente", "Incluye el concepto de Validez Divergente"]
    },
    "Validez de Criterio": {
        "area": "Investigación", 
        "correctos": ["Abarca los tipos Concurrente y Predictiva", "Requiere comparación contra un Estándar de Oro", "Busca una Correlación externa verificable", "Demuestra Eficacia de pronóstico del instrumento"]
    },
    "Medidas de Tendencia Central": {
        "area": "Investigación", 
        "correctos": ["Cálculo de la Media aritmética (Promedio)", "Cálculo de la Mediana (Punto medio exacto)", "Cálculo de la Moda (Valor más frecuente)", "Buscan resumir un conjunto de datos en un solo valor"]
    },
    "Medidas de Dispersión": {
        "area": "Investigación", 
        "correctos": ["Desviación Estándar poblacional", "Cálculo de Varianza", "Amplitud de Rango", "Indican nivel de dispersión respecto a la media"]
    },
    "Enfoque Fenomenológico": {
        "area": "Investigación", 
        "correctos": ["Estudia la experiencia humana vivida", "Analiza el significado subjetivo profundo", "Utiliza entrevistas no estructuradas o a profundidad", "Pertenece a la rama de Investigación Cualitativa"]
    },
    "Consentimiento Informado": {
        "area": "Investigación", 
        "correctos": ["Garantiza el principio ético de Voluntariedad", "Exige explicación clara y prospectiva de riesgos", "Protege el Derecho inalienable a retirarse", "Requiere Firma o asentimiento documentado del menor"]
    }
}
