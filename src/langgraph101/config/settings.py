from __future__ import annotations

from dataclasses import dataclass
import os


@dataclass(frozen=True)
class OllamaSettings:
    base_url: str = os.getenv("OLLAMA_BASE_URL", "http://127.0.0.1:11434")
    model: str = os.getenv("OLLAMA_MODEL", "llama3.2:latest")
    temperature: float = float(os.getenv("OLLAMA_TEMPERATURE", "0"))


ollama_settings = OllamaSettings()


