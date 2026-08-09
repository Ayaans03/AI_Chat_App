from fastapi import FastAPI
from app.schemas.chat import Message, Prompt
from app.core.database import check_postgres_connection
from app.services.llm_service import interaction
app = FastAPI()

@app.get('/get_api')
def read_root():
    return {"Hello": "World"}

@app.post('/message')
def post_message(data: Message):
    return data

@app.post('/prompt')
def prompt_ai(data: Prompt):
    response = interaction(data.text)
    return response

@app.get('/check-postgre-db')
def progre_db():
    status = check_postgres_connection()
    return status
