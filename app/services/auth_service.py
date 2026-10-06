from app.core.security import hash_password
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.user import User
from app.core.database import engine

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