from fastapi import APIRouter
from app.services.auth_service import register_user
from fastapi import HTTPException
from app.schemas.auth import User, Token
from fastapi.responses import JSONResponse
from app.services.auth_service import user_login

router = APIRouter(
    prefix= "/auth",
    tags= ["auth"]
)

@router.post("/register")
def register(data: User):
    try:
        request = register_user(data.email, data.password)
        return JSONResponse(request)
    except HTTPException as e:
        print(e)

@router.post("/login", response_model=list[Token])
def login(data: User):
    try:
        request = user_login(data.email, data.password)
        return JSONResponse(request)
    except HTTPException as e:
        print(e)