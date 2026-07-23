from fastapi import FastAPI
from app.schemas.chat import Message
app = FastAPI()

@app.get('/get_api')
def read_root():
    return {"Hello": "World"}

@app.post('/message')
def post_message(data: Message):
    return data
