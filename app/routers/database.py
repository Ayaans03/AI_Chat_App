from fastapi import APIRouter
from app.services.database_service import check_postgres_connection, get_chat_hisotry_from_message_table
from fastapi.responses import JSONResponse
from fastapi import HTTPException
from app.schemas.database import MessageResponse

router = APIRouter(
    prefix= "/database",
    tags= ["database"]
)

@router.get('/check_postgre_db')
def postgre_db():
    try:
        status = check_postgres_connection()
        return {"Message": "Connected to database s"}
    except HTTPException as e:
        print(e)

@router.get('/get_chat_history', response_model=list[MessageResponse])
def chat_history():
    try:
        history = get_chat_hisotry_from_message_table()
        return history
    except HTTPException as e:
        print(e)