from fastapi import FastAPI
from .routers import chat, database

app = FastAPI()

app.include_router(chat.router)
app.include_router(database.router)