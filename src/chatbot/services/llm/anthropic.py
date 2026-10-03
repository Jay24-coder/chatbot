from src.chatbot.services.llm.base import LLMProvider
from anthropic import Anthropic

class Anthropic(LLMProvider):
    def __init__(self, api_key):
        self.client = Anthropic(api_key=api_key)

    def text_output(self, model: str, prompt: str, message: str):
        response = self.client.messages.create(
            model=model,
            max_tokens=1024,
            messages=[
                {
                    "role": "developer",
                    "content": prompt
                },
                {
                    "role": "user",
                    "content": message
                }
            ]
        )

        return response[0].text