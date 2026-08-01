import json

from google import genai
from google.genai import types

from app.core.config import settings
from app.prompts.system_prompt import SYSTEM_PROMPT


class GeminiService:

    def __init__(self):
        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

    def generate_response(self, question: str, knowledge: dict):

        context = json.dumps(
            knowledge,
            ensure_ascii=False,
            indent=2
        )

        prompt = f"""
{SYSTEM_PROMPT}

INFORMACIÓN DISPONIBLE

{context}

PREGUNTA

{question}
"""

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.4
            )
        )

        return response.text