from fastapi import APIRouter
from app.services.llm_service import chat_and_update_in_db
from fastapi.responses import JSONResponse
from fastapi import HTTPException, Depends
from app.core.security import get_current_user
from app.schemas.chat import Chat

router = APIRouter(
    prefix = "/chat",
    tags = ["chat"]
)

@router.post("/chat_with_ai")
def chat_with_ai(data: Chat, Token: str = Depends(get_current_user)):
    try:
        request = chat_and_update_in_db(data.text)
        return JSONResponse(request)
    except HTTPException as e:
        print(e)