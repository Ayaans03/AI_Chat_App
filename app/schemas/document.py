from pydantic import BaseModel

# Validation to request body to chat
class Document(BaseModel):
    text: str