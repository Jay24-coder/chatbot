from chatbot.services.llm import llama_cpp
from chatbot.services.llm.base import LLMProvider
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

from src.chatbot.services.llm.anthropic import Anthropic
from src.chatbot.services.llm.openrouter import OpenRouter
from src.chatbot.services.llm.llama_cpp import LlamaCpp


MODEL_PROVIDER="llama_cpp"


class Settings(BaseSettings):
    anthropic_api_key: Optional[str]
    openrouter_api_key: Optional[str]
    openrouter_url: Optional[str]
    llama_cpp_url: Optional[str]
    
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
        encodings="utf-8"
    )


def get_model_provider_client(settings: Settings) -> LLMProvider:
    if MODEL_PROVIDER == "llama_cpp":
        return LlamaCpp(url=settings.llama_cpp_url)

    elif MODEL_PROVIDER == "anthropic":
        return Anthropic(api_key=settings.anthropic_api_key)

    elif MODEL_PROVIDER == "openrouter":
        return OpenRouter(url=settings.openrouter_url, api_key=settings.openrouter_api_key)

    else:
        raise "No LLM provider configured"

