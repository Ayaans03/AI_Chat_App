from pydantic import BaseModel 
from datetime import datetime

class MessageResponse(BaseModel):
    id: int
    role: str
    content: str
    created_at: datetime
    conversation_id : int