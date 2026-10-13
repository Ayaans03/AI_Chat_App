from pydantic import BaseModel
from datetime import timedelta

class User(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
    token_expiration: str