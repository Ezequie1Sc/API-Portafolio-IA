from fastapi import FastAPI, HTTPException

from app.api import chat_router
from app.core.config import settings
from app.core.security import configure_cors
from app.services.gemini_service import GeminiService

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.API_VERSION,
)

configure_cors(app)

app.include_router(chat_router)

gemini_service = GeminiService()


@app.get("/")
async def root():
    return {
        "message": "Portfolio IA API",
        "status": "running"
    }


@app.get("/test-gemini")
async def test_gemini():
    try:
        response = gemini_service.client.models.generate_content(
            model="gemini-2.5-flash",
            contents="Responde únicamente: OK"
        )

        return {
            "respuesta": response.text
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@app.get("/models")
async def list_models():
    try:
        models = [
            model.name
            for model in gemini_service.client.models.list()
        ]

        return {
            "total": len(models),
            "models": models
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )