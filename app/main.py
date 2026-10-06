from fastapi import FastAPI
from .routers import chat, database, auth

app = FastAPI()

app.include_router(chat.router)
app.include_router(database.router)
app.include_router(auth.router)