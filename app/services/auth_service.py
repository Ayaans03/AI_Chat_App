from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.user import User
from app.core.database import engine
from sqlalchemy import select
from app.core.database import _engine_connect
from app.models.user import User
from app.core.security import hash_password, verify_password, create_access_token, create_referesh_token, decode_token
from datetime import timedelta
from app.core.config import settings

def register_user(user_email: str, user_password: str):
    try:
        register = User(
            email = user_email,
            hased_password = hash_password(user_password)
        )

        session = Session(engine)
        session.add(register)
        session.commit()
        return {"Message": "User is been registered"}
    except HTTPException as e:
        print(e)


def user_login(user_email: str, user_password: str):
    try:
        with _engine_connect() as Connection:
            email, password = Connection.execute(select(User.email, User.hased_password)).first()
            if email == user_email and  verify_password(user_password,password):
                access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
                refresh_token_expires = timedelta(hours=settings.refresh_token_expire_hours)
                access_token = create_access_token(data= {"sub": email}, expires_delta=access_token_expires)
                referesh_token = create_referesh_token(data= {"sub":email}, expires_delta=refresh_token_expires)
                return {
                    "Access_token": access_token,
                    "Token_type": "Bearer",
                    "Access_Token_expiration": str(access_token_expires),
                    "Refresh_token": referesh_token,
                    "Refresh_Token_expiration":str(refresh_token_expires)
                }
            else:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password", headers={"WWW-Authenticate":"Bearer"})
    except HTTPException as e:
        raise e

def get_new_access_token(refresh_token: str):
    try:
        payload = decode_token(refresh_token)
        if "token_type" not in payload or payload["token_type"] != "refresh":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail= "Invalid refresh token",
                headers={"WWW-Authenticate": "Bearer"}
            )
        email = payload.get("sub")
        if email is None:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail= "Could Not validate credentials",
                headers= {"WWW-Authenticate": "Bearer"}
            )
        access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
        access_token  = create_access_token(data= {"sub": email}, expires_delta=access_token_expires)
        return {
            "Access_token": access_token,
            "Token_type": "Bearer",
            "Access_Token_expiration": str(access_token_expires)
        }
    except HTTPException as e:
        raise e    