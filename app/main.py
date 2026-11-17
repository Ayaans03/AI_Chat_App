from fastapi import FastAPI
from .routers import chat, database, auth, coversation, document

app = FastAPI()

app.include_router(chat.router)
app.include_router(database.router)
app.include_router(auth.router)
app.include_router(coversation.router)
app.include_router(document.router)