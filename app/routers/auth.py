from fastapi import APIRouter
from app.services.auth_service import register_user
from fastapi import HTTPException
from app.schemas.auth import Register_User
from fastapi.responses import JSONResponse

router = APIRouter(
    prefix= "/auth",
    tags= ["auth"]
)

@router.post("/register")
def register(data: Register_User):
    try:
        request = register_user(data.email, data.password)
        return JSONResponse(request)
    except HTTPException as e:
        print(e)