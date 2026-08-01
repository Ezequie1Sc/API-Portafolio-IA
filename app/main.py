from fastapi import FastAPI

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