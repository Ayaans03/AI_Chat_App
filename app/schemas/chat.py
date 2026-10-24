from pydantic import BaseModel

# Validation to request body to chat
class Chat(BaseModel):
    text: str
    conversation_id : int