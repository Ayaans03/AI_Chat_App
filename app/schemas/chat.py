from pydantic import BaseModel

class Message(BaseModel):
    post_message: str