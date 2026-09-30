from sqlalchemy import create_engine,text
from fastapi import HTTPException
from app.core.database import engine

# Function to check the database connection by running simple query
def check_postgres_connection():
    try:
        with engine.connect() as Connection:
            Connection.execute(text("select 1"))
            return {"message":"Connected Successfully"}
    except HTTPException as e:
        print(e)