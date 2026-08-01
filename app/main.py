from fastapi import FastAPI
from google import genai

from app.api import chat_router
from app.core.config import settings
from app.core.security import configure_cors

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.API_VERSION,
)

configure_cors(app)

app.include_router(chat_router)


@app.get("/")
async def root():
    return {
        "message": "Portfolio IA API",
        "status": "running"
    }

from fastapi import HTTPException
from google import genai

@app.get("/test-gemini")
async def test_gemini():
    try:
        client = genai.Client(api_key=settings.GEMINI_API_KEY)

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents="Responde únicamente: OK"
        )

        return {"respuesta": response.text}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))