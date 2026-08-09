from dotenv import load_dotenv
import os
from sqlalchemy import create_engine,text
from fastapi import HTTPException

load_dotenv()

POSTGRES_CONNECTION_STRING=os.getenv("POSTGRES_CONNECTION_STRING")

def check_postgres_connection():
    engine = create_engine(POSTGRES_CONNECTION_STRING)
    with engine.connect() as Connection:
        result = Connection.execute(text("select 1"))
        return {"message":"Connected Successfully","result":result}
