from app.models.chat_intent import ChatIntent


class ContextBuilder:

    def build(
        self,
        question: str,
        intent: ChatIntent,
        data,
        personality: dict
    ) -> str:

        identity = personality["assistant_identity"]
        communication = personality["communication"]
        rules = personality["rules"]

        prompt = f"""
Eres {identity["role"]}.

OBJETIVO
{identity["objective"]}

ESTILO

Tono: {communication["tone"]}
Estilo: {communication["style"]}
Longitud: {communication["response_length"]}

REGLAS
"""

        for rule in rules:
            prompt += f"- {rule}\n"

        # ==========================================
        # REGLAS ESPECÍFICAS POR INTENT
        # ==========================================

        # ==========================================
        # PROFILE - CARD
        # ==========================================

        if intent == ChatIntent.PROFILE:

            prompt += """

IMPORTANTE

El frontend mostrará automáticamente una tarjeta
visual con la información completa del perfil.

NO repitas:

- Nombre
- Correo
- Teléfono
- Ubicación
- Tecnologías
- Habilidades
- Información detallada del perfil

Responde únicamente con una breve introducción de
máximo 2 líneas.

Ejemplo:

"👋 ¡Claro! Aquí tienes mi perfil profesional."

"""

        # ==========================================
        # GITHUB - CARD
        # ==========================================

        elif intent == ChatIntent.GITHUB:

            prompt += """

IMPORTANTE

El frontend mostrará automáticamente una tarjeta
visual de GitHub.

NO repitas:

- Usuario
- URL
- Repositorios
- Contribuciones
- Enlaces

Responde únicamente con una breve introducción.

Ejemplo:

"💻 Aquí puedes explorar mi perfil oficial de GitHub."

"""

        # ==========================================
        # SKILLS - CARD
        # ==========================================

        elif intent == ChatIntent.SKILL:

            prompt += """

IMPORTANTE

El frontend mostrará automáticamente una tarjeta
visual con las tecnologías y habilidades.

NO enumeres nuevamente todas las tecnologías.

NO escribas el stack completo.

NO hagas una lista de habilidades.

Responde únicamente con una breve introducción.

Ejemplo:

"🚀 Estas son las tecnologías y herramientas con las
que trabajo actualmente."

"""

        # ==========================================
        # PROJECTS - TEXTO NORMAL
        # ==========================================

        elif intent == ChatIntent.PROJECT:

            prompt += """

IMPORTANTE

El usuario está preguntando por proyectos.

Projects NO se muestra como una tarjeta visual.

Responde normalmente utilizando únicamente la
información proporcionada.

Puedes mencionar:

- Nombre del proyecto
- Tipo de proyecto
- Tecnologías
- Descripción
- Funcionalidades
- Categoría
- Información relevante disponible

Si el usuario pregunta por varios proyectos,
puedes presentar la información de forma clara
y organizada.

No inventes proyectos ni tecnologías.

"""

        # ==========================================
        # CERTIFICATIONS - TEXTO NORMAL
        # ==========================================

        elif intent == ChatIntent.CERTIFICATION:

            prompt += """

IMPORTANTE

El usuario está preguntando por certificaciones.

Las certificaciones NO se muestran como una tarjeta
visual.

Responde normalmente utilizando la información
proporcionada.

Puedes mencionar:

- Nombre de la certificación
- Institución
- Año
- Categoría
- Descripción
- Temas aprendidos
- Habilidades adquiridas

Si el usuario pregunta por una certificación
específica, responde únicamente utilizando los
datos disponibles de esa certificación.

Si pregunta por certificaciones de un área específica,
filtra la información correspondiente.

Nunca inventes certificaciones, instituciones,
fechas o habilidades.

"""

        # ==========================================
        # CONTACT - TEXTO NORMAL
        # ==========================================

        elif intent == ChatIntent.CONTACT:

            prompt += """

IMPORTANTE

El usuario está preguntando por información de contacto.

No existe una tarjeta visual especial para contacto.

Responde normalmente utilizando únicamente la
información proporcionada.

Puedes mencionar correo, teléfono, ubicación u otros
medios de contacto cuando el usuario los solicite.

"""

        # ==========================================
        # EDUCATION - TEXTO NORMAL
        # ==========================================

        elif intent == ChatIntent.EDUCATION:

            prompt += """

IMPORTANTE

El usuario está preguntando por formación académica.

No existe una tarjeta visual especial para educación.

Responde normalmente utilizando únicamente la
información proporcionada.

Puedes mencionar institución, carrera, grado,
formación y demás información disponible.

"""

        # ==========================================
        # EXPERIENCE - TEXTO NORMAL
        # ==========================================

        elif intent == ChatIntent.EXPERIENCE:

            prompt += """

IMPORTANTE

El usuario está preguntando por experiencia profesional.

No existe una tarjeta visual especial para experiencia.

Responde normalmente utilizando únicamente la
información proporcionada.

Puedes mencionar empresas, puestos, responsabilidades,
tecnologías y experiencia relevante.

"""

        # ==========================================
        # INFORMACIÓN FINAL
        # ==========================================

        prompt += f"""

INTENCIÓN
{intent.value}

PREGUNTA
{question}

INFORMACIÓN DISPONIBLE
{data}

RESPUESTA

Responde únicamente utilizando la información
proporcionada.

Si la información no existe, indícalo claramente.

No inventes datos.

"""

        return prompt