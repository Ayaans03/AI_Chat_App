from sqlalchemy.orm import Session
from app.models.conversation import Conversation
from app.core.database import engine
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