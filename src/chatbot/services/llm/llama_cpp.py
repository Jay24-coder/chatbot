from ast import mod
from openai import OpenAI
from src.chatbot.services.llm.base import LLMProvider


class LlamaCpp(LLMProvider):
    def __init__(self, url, api_key: str = None):
        self.client = OpenAI(base_url=self.url, api_key=self.api)

    def text_output(self, model, prompt, message):
        response = self.client.response.create(
            model=model,
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