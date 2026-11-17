from sqlalchemy import select
from fastapi import HTTPException
from app.core.database import _engine_connect

# Function to check the database connection by running simple query
def check_postgres_connection():
    try:
        with _engine_connect() as Connection:
            Connection.execute(select(1)).all()
            return {"Message": "Connected to databases"}
    except HTTPException as e:
        raise e