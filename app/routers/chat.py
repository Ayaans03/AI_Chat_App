from fastapi import APIRouter
from app.services.llm_service import chat_and_update_in_db
from fastapi import HTTPException, Depends
from app.schemas.chat import Chat
from app.schemas.database import MessageResponse
from app.services.llm_service import get_chat_history_from_message_table
from app.core.redis import rate_limiting

router = APIRouter(
    prefix = "/chat",
    tags = ["chat"]
)

@router.post("/chat_with_ai")
def chat_with_ai(data: Chat , Usage: str = Depends(rate_limiting)):
    try:
        request = chat_and_update_in_db(data.text, data.conversation_id)
        return request
    except HTTPException as e:
        raise e

@router.get('/get_chat_history/{conversation_id}', response_model=list[MessageResponse])
def chat_history(conversation_id: int):
    try:
        history = get_chat_history_from_message_table(conversation_id)
        return history
    except HTTPException as e:
        raise e