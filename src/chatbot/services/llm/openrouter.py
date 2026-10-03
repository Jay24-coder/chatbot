from src.chatbot.services.llm.base import LLMProvider
from openai import OpenAI


class OpenRouter(LLMProvider):
    def __init__(self, url, api_key):
        self.url = url
        self.api_key = api_key
        self.client = OpenAI()

    def text_output(self, model: str, prompt: str, message: str):
        response = self.client.responses.create(
            model = model,
            input=[
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
        return response.output_text
