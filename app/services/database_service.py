from sqlalchemy import create_engine,text
from fastapi import HTTPException
from app.core.config import settings

# Function to check the database connection by running simple query
def check_postgres_connection():
    try:
        engine = create_engine(settings.postgres_connection_string)
        with engine.connect() as Connection:
            result = Connection.execute(text("select 1"))
            return {"message":"Connected Successfully","result":result}
    except HTTPException as e:
        print(e)