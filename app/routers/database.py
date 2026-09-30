from fastapi import APIRouter
from app.services.database_service import check_postgres_connection
from fastapi.responses import JSONResponse
from fastapi import HTTPException

router = APIRouter(
    prefix= "/database",
    tags= ["database"]
)

@router.get('/check_postgre_db')
def postgre_db():
    try:
        status = check_postgres_connection()
        return JSONResponse(status)
    except HTTPException as e:
        print(e)