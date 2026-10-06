from pydantic import BaseModel

class Register_User(BaseModel):
    email: str
    password: str