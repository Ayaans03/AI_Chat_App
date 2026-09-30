from pydantic import BaseModel, ValidationError, PydanticUserError

# Validation to request body to chat
class Chat(BaseModel):
    text: str

try:
    Chat()
except ValidationError as e:
    print(repr(e.errors()[0]['type']))
except PydanticUserError as e:
    print(repr(e.errors()[0]['type']))