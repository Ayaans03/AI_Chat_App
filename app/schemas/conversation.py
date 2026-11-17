from pydantic import BaseModel
from datetime import datetime

class Conversation_Id_Response(BaseModel):
    id : int
    created_at: datetime
    user_id: int