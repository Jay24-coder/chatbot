from fastapi import APIRouter
from src.chatbot.schema.user_request import UserRequest


chatbot_router = APIRouter()

@chatbot_router.post("/chatbot", tags=["chat"])
def chat(user_request: UserRequest):
    return {
        "user_query": user_request.message,
        "response": "This is a response to your message",
        "status": 200
    }

