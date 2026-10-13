from sqlalchemy import select
from fastapi import HTTPException
from app.core.database import engine
from app.models.message import Message
from app.core.database import _engine_connect
# Function to check the database connection by running simple query
def check_postgres_connection():
    try:
        with _engine_connect() as Connection:
            Connection.execute(select(1)).all()
            return {"Message": "Connected to databases"}
    except HTTPException as e:
        print(e)

def get_chat_hisotry_from_message_table():
    try:
        with _engine_connect() as Connection:
            result = Connection.execute(select(Message).order_by(Message.id.asc()).offset(offset=0).limit(limit=100)).all()
            return result

    except HTTPException as e:
        print(e)