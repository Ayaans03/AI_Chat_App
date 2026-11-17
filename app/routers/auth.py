from fastapi import APIRouter
from app.services.auth_service import register_user
from fastapi import HTTPException
from app.schemas.auth import User, Token, Refresh_Token
from fastapi.responses import JSONResponse
from app.services.auth_service import user_login, get_new_access_token

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
        raise e

@router.post("/login", response_model=list[Token])
def login(data: User):
    try:
        request = user_login(data.email, data.password)
        return JSONResponse(request)
    except HTTPException as e:
        raise e

@router.post("/refresh_token", response_model=list[Token])
def token_refresh(data: Refresh_Token):
    try:
        request = get_new_access_token(data.refresh_token)
        return JSONResponse(request)
    except HTTPException as e:
        raise e