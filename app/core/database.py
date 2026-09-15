from dotenv import load_dotenv
import os
from sqlalchemy import create_engine,text
from fastapi import HTTPException
from app.models.user import Base

load_dotenv()

POSTGRES_CONNECTION_STRING=os.getenv("POSTGRES_CONNECTION_STRING")

def check_postgres_connection():
    try:
        engine = create_engine(POSTGRES_CONNECTION_STRING)
        with engine.connect() as Connection:
            result = Connection.execute(text("select 1"))
            return {"message":"Connected Successfully","result":result}
    except HTTPException as e:
        print(e)

engine = create_engine(POSTGRES_CONNECTION_STRING)
Base.metadata.create_all(bind=engine)
print("Database initialized")