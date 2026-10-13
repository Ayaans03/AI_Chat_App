from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.user import User
from app.core.database import engine
from sqlalchemy import select
from app.core.database import _engine_connect
from app.models.user import User
from app.core.security import hash_password, verify_password, create_access_token
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
                print("Debugging time:",access_token_expires)
                access_token = create_access_token(data= {"sub": email}, expires_delta=access_token_expires)
                return {
                    "Access_token": access_token,
                    "Token_type": "bearer",
                    "Token_expiration": str(access_token_expires)
                }
            else:
                return {"Message": "Invalid Email or Password"}
    except HTTPException as e:
        print(e)
    