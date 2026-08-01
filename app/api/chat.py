from fastapi import APIRouter, HTTPException

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.gemini_service import GeminiService
from app.services.knowledge_service import KnowledgeService

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

knowledge_service = KnowledgeService()
gemini_service = GeminiService()


@router.post(
    "",
    response_model=ChatResponse
)
async def chat(request: ChatRequest):

    try:

        knowledge = knowledge_service.search(
            request.message
        )

        response = gemini_service.generate_response(
            request.message,
            knowledge
        )

        return ChatResponse(
            response=response
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )