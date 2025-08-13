from __future__ import annotations
from pydantic import BaseModel
from typing import List
from langchain_core.messages import AnyMessage
from langchain_core.runnables import RunnableConfig
from langgraph.prebuilt import create_react_agent
from langgraph.prebuilt.chat_agent_executor import AgentState

from ..models.ollama import create_ollama_chat_model
from ..tools.weather import get_weather

class WeatherResponse(BaseModel):
    conditions: str

def build_default_react_agent():
    model = create_ollama_chat_model()
    return create_react_agent(
        model=model,
        tools=[get_weather],
        prompt="You are a helpful assistant",
        response_format=WeatherResponse,
    )


def build_personalized_react_agent():
    model = create_ollama_chat_model()

    def system_prompt(state: AgentState, config: RunnableConfig) -> List[AnyMessage]:
        user_name = config["configurable"].get("user_name")
        system_msg = f"You are a helpful assistant. Address the user as {user_name}."
        return [{"role": "system", "content": system_msg}] + state["messages"]

    return create_react_agent(
        model=model,
        tools=[get_weather],
        prompt=system_prompt,
    )


