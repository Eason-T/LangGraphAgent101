from __future__ import annotations

from langchain_ollama import ChatOllama
from ..config.settings import ollama_settings


def create_ollama_chat_model() -> ChatOllama:
    return ChatOllama(
        model=ollama_settings.model,
        temperature=ollama_settings.temperature,
        base_url=ollama_settings.base_url,
    )


