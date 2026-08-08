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

        if intent == ChatIntent.PROFILE:

            prompt += """

IMPORTANTE

El frontend mostrará automáticamente una tarjeta visual del perfil.

NO repitas:

- Nombre
- Correo
- Teléfono
- Ubicación
- Tecnologías
- Habilidades

Responde únicamente con una breve introducción (máximo 2 líneas).

Ejemplo:

"¡Con gusto! 😊
Aquí tienes mi perfil profesional."

"""

        elif intent == ChatIntent.GITHUB:

            prompt += """

IMPORTANTE

El frontend mostrará automáticamente una tarjeta de GitHub.

NO escribas:

- Usuario
- Enlaces
- Repositorios
- Contribuciones

Responde únicamente con una breve introducción.

Ejemplo:

"💻 Aquí puedes explorar mi perfil oficial de GitHub."

"""

        elif intent == ChatIntent.SKILL:

            prompt += """

IMPORTANTE

El frontend mostrará automáticamente la tarjeta de tecnologías.

NO enumeres tecnologías.

NO escribas el stack.

NO describas habilidades.

Solo escribe una introducción.

Ejemplo:

"🚀 Estas son las tecnologías con las que trabajo actualmente."

"""

        elif intent == ChatIntent.PROJECT:

            prompt += """

IMPORTANTE

El usuario está preguntando por proyectos.

Puedes describir el proyecto solicitado normalmente.

"""

        elif intent == ChatIntent.CONTACT:

            prompt += """

IMPORTANTE

El frontend mostrará automáticamente la tarjeta de contacto.

No repitas correo, teléfono o ubicación.

Solo invita al usuario a ponerse en contacto.

"""

        elif intent == ChatIntent.EDUCATION:

            prompt += """

IMPORTANTE

El frontend mostrará automáticamente la tarjeta de educación.

No enumeres nuevamente los estudios.

Solo escribe una breve introducción.

"""

        elif intent == ChatIntent.EXPERIENCE:

            prompt += """

IMPORTANTE

El frontend mostrará automáticamente la tarjeta de experiencia.

No repitas toda la experiencia.

Solo escribe una breve introducción.

"""

        elif intent == ChatIntent.CERTIFICATION:

            prompt += """

IMPORTANTE

El frontend mostrará automáticamente la tarjeta de certificaciones.

No vuelvas a listar las certificaciones.

Solo escribe una breve introducción.

"""

        prompt += f"""

INTENCIÓN
{intent.value}

PREGUNTA
{question}

INFORMACIÓN
{data}

RESPUESTA

Responde únicamente utilizando la información proporcionada.

Si la información no existe, indícalo claramente.

No inventes datos.

"""

        return prompt