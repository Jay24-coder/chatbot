from fastapi import FastAPI
from src.chatbot.api.router.health import health_router
from src.chatbot.api.router.chatbot import chatbot_router


app = FastAPI()

app.include_router(health_router)
app.include_router(chatbot_router)