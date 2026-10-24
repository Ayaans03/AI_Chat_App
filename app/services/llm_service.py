from google.genai import Client, errors
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.message import Message
from app.models.conversation import Conversation # import to recognized relationship for message and conversation table by the prompt_ai function
from app.core.config import settings
from app.core.database import engine, _engine_connect
from app.models.message import Message
from sqlalchemy import select
from google.genai import types

client = Client(api_key=settings.gemini_api_key)

def get_chat_history_from_message_table(conversation_id):
    try:
        with _engine_connect() as Connection:
            result = Connection.execute(select(Message).where(Message.conversation_id==conversation_id).order_by(Message.created_at.asc()).offset(offset=0).limit(limit=10)).all()
            return result

    except HTTPException as e:
        raise e

# LLM function so that it can be used by all
def initialize_llm(data, conversation_id: int):
    try:
        history_list = []
        conv_history=get_chat_history_from_message_table(conversation_id)

        for msg_history in conv_history:
            history_list.append(types.Content(
                role=msg_history.role,
                parts=[types.Part.from_text(text=msg_history.content)]
            ))

        interact = client.chats.create(
            model="gemini-3.5-flash-lite",
            history=history_list
        )
        response = interact.send_message(data)
        return response.candidates[0].content.parts[0].text
    except (errors.ClientError, errors.ServerError) as e:
        raise e

# Logic to chat and insert the conversation history in the message table
def chat_and_update_in_db(prompt: str, converstaion_id: int):
    try:
        session = Session(engine)
        user = Message(
            role = "user",
            content = prompt,
            conversation_id = converstaion_id
        )

        response = initialize_llm(prompt, converstaion_id)
        assistent = Message(
            role = "model",
            content = response,
            conversation_id = converstaion_id
            )

        session.add(user)
        session.add(assistent)
        session.commit()
        return response

    except HTTPException as e:
        raise e