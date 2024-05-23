from fastapi import FastAPI
from .routers import chatbot

app = FastAPI()

app.include_router(chatbot.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Music Gear Chatbot!"}
