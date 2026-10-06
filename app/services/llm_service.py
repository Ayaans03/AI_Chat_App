from google.genai import Client, errors
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.core.database import engine
from app.models.message import Message
from app.models.conversation import Conversation # import to recognized relationship for message and conversation table by the prompt_ai function
from app.core.config import settings

client = Client(api_key=settings.gemini_api_key)

# LLM function so that it can be used by all
def initialize_llm(data):
    try:
        interact = client.interactions.create(
            model="gemini-2.5-flash",
            input=data
        )
        return interact.output_text
    except [errors.ClientError, errors.ServerError] as e:
        raise HTTPException(status_code=[i for i in range(400,600)])

# Logic to chat and insert the conversation history in the message table
def chat_and_update_in_db(data: str):
    try:
        session = Session(engine)
        user = Message(
            role = "user",
            content = data,
            conversation_id = 3
        )
        session.add(user)

        response = initialize_llm(data)
        assistent = Message(
            role = "assistent",
            content = response,
            conversation_id = 3
            )

        session.add(assistent)

        session.commit()
        return response
    except HTTPException as e:
        print(e)