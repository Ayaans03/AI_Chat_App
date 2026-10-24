from sqlalchemy.orm import Session
from app.models.conversation import Conversation
from app.core.database import engine, _engine_connect
from sqlalchemy import select
from fastapi import HTTPException

def get_conversation_id(user_id):
    try:
        session = Session(engine)
        conversation_id = Conversation(
            user_id = user_id
        )
        session.add(conversation_id)
        session.commit()
        session.refresh(conversation_id)
        return conversation_id
    except HTTPException as e:
        raise e

def get_all_conversation(user_id):
    try:
        with _engine_connect() as Connection:
            result = Connection.execute(select(Conversation).where(Conversation.user_id==user_id)).all()
            return result
    except HTTPException as e:
        raise e