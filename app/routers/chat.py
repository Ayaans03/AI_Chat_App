from fastapi import APIRouter
from app.services.llm_service import chat_and_update_in_db
from fastapi.responses import JSONResponse
from fastapi import HTTPException, Depends
from app.core.security import get_current_user
from app.schemas.chat import Chat, Chat_Response
from app.schemas.database import MessageResponse
from app.services.llm_service import get_chat_hisotry_from_message_table

router = APIRouter(
    prefix = "/chat",
    tags = ["chat"]
)

@router.post("/chat_with_ai", response_model=Chat_Response)
def chat_with_ai(data: Chat, Token: str = Depends(get_current_user)):
    try:
        request = chat_and_update_in_db(data.text, data.conversation_id)
        return JSONResponse(request)
    except HTTPException as e:
        raise e

@router.get('/get_chat_history', response_model=MessageResponse)
def chat_history():
    try:
        history = get_chat_hisotry_from_message_table()
        return history
    except HTTPException as e:
        raise e