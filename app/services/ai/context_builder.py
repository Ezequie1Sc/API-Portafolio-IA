import json


class ContextBuilder:

    def build(
        self,
        question: str,
        intent: str,
        data: dict | list,
        rules: dict
    ) -> str:

        context = f"""
# INSTRUCCIONES

{json.dumps(rules, indent=2, ensure_ascii=False)}

# INTENCIÓN

{intent}

# PREGUNTA

{question}

# INFORMACIÓN

{json.dumps(data, indent=2, ensure_ascii=False)}

# RESPUESTA

Responde únicamente utilizando la información proporcionada.
No inventes datos.
Si la información no existe, indícalo claramente.
"""

        return context