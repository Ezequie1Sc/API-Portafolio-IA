from google import genai
from google.genai import types

from app.core.config import settings


class GeminiService:

    def __init__(self):

        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

    def list_models(self):

        return [
            model.name
            for model in self.client.models.list()
        ]

    def generate(self, prompt: str) -> str:

        response = self.client.models.generate_content(

            model="gemini-2.5-flash",

            contents=prompt,

            config=types.GenerateContentConfig(

                temperature=0.3,

                max_output_tokens=600

            )

        )

        return response.text