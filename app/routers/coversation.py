from fastapi import APIRouter
from app.services.conversation import get_conversation_id
from fastapi import HTTPException, Depends
from app.core.security import get_current_user
from app.schemas.conversation import Conversation_Id_Response

router = APIRouter(
    prefix= "",
    tags = ["conversation"]
)

@router.post("/conversations", response_model=Conversation_Id_Response)
def get_chat_conersation_id(Token: tuple = Depends(get_current_user)):
    try:
        request = get_conversation_id(Token[1])
        return request
    except HTTPException as e:
        raise e