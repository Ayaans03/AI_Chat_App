from pydantic import BaseModel, ValidationError

class Message(BaseModel):
    post_message: str

class Prompt(BaseModel):
    text: str

try:
    Prompt()
except ValidationError as e:
    print(repr(e.errors()[0]['type']))