from __future__ import annotations

from typing import Any, Dict, List, Optional
from langchain_core.messages import AIMessage, ToolMessage


def extract_useful_info(state: Dict[str, Any]) -> Dict[str, Any]:
    messages = state.get("messages", [])
    final_ai_message: Optional[AIMessage] = None
    tool_calls: List[dict] = []
    tool_outputs: List[dict] = []

    for message in messages:
        if isinstance(message, AIMessage):
            final_ai_message = message
            current_tool_calls = getattr(message, "tool_calls", None)
            if current_tool_calls:
                tool_calls.extend(current_tool_calls)
        elif isinstance(message, ToolMessage):
            tool_outputs.append({
                "name": getattr(message, "name", None),
                "content": message.content,
                "tool_call_id": getattr(message, "tool_call_id", None),
            })

    final_text = None
    usage_metadata = None
    if final_ai_message is not None:
        content = final_ai_message.content
        final_text = content if isinstance(content, str) else str(content)
        usage_metadata = getattr(final_ai_message, "usage_metadata", None)

    return {
        "final_text": final_text,
        "tool_calls": tool_calls,
        "tool_outputs": tool_outputs,
        "usage": usage_metadata,
    }


