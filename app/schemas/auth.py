from pydantic import BaseModel

class User(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
    access_token_expiration: str
    refresh_token: str
    refresh_token_expiration: str

class Refresh_Token(BaseModel):
    refresh_token: str