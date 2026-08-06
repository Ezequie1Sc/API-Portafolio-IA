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