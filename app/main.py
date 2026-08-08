from fastapi import FastAPI, HTTPException

from app.api import (
    chat_router,
    knowledge_router,
)

from app.core.config import settings
from app.core.security import configure_cors
from app.services.ai.gemini_service import GeminiService


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.API_VERSION,
)

configure_cors(app)

# =====================================================
# Routers
# =====================================================

app.include_router(chat_router)
app.include_router(knowledge_router)

# =====================================================
# Services
# =====================================================

gemini_service = GeminiService()

# =====================================================
# Root
# =====================================================

@app.get("/")
async def root():
    return {
        "application": settings.APP_NAME,
        "version": settings.API_VERSION,
        "status": "running",
        "documentation": {
            "swagger": "/docs",
            "redoc": "/redoc"
        },
        "endpoints": {
            "chat": {
                "method": "POST",
                "url": "/chat"
            },
            "knowledge": {
                "profile": "/knowledge/profile",
                "skills": "/knowledge/skills",
                "github": "/knowledge/github"
            },
            "utilities": {
                "test_gemini": "/test-gemini",
                "models": "/models"
            }
        }
    }

# =====================================================
# Test Gemini
# =====================================================

@app.get("/test-gemini")
async def test_gemini():

    try:

        response = gemini_service.client.models.generate_content(
            model="gemini-2.5-flash",
            contents="Responde únicamente: OK"
        )

        return {
            "status": "success",
            "response": response.text
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

# =====================================================
# Available Models
# =====================================================

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