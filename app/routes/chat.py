from fastapi import APIRouter
from app.services.chat_service import get_chat_response
from app.schemas.chat import ChatRequest

router = APIRouter(prefix="/chat",tags=['Chat'])

@router.post("")
async def start_chat(data: ChatRequest):
    return await get_chat_response(data.query)
