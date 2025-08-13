from __future__ import annotations

import argparse
from typing import Optional

from ..agents.react_agent import build_default_react_agent, build_personalized_react_agent
from ..utils.messages import extract_useful_info


def run(query: str, user_name: Optional[str] = None) -> None:
    if user_name:
        agent = build_personalized_react_agent()
        state = agent.invoke({"messages": [{"role": "user", "content": query}]}, config={"configurable": {"user_name": user_name}})
    else:
        agent = build_default_react_agent()
        state = agent.invoke({"messages": [{"role": "user", "content": query}]})

    summary = extract_useful_info(state)
    response = state
    # print(response.get("messages", [])[-1].content)
    # print(summary["final_text"])


def main() -> None:
    parser = argparse.ArgumentParser(description="LangGraph101 CLI")
    parser.add_argument("query", type=str, help="User query")
    parser.add_argument("--user", dest="user", type=str, default=None, help="User name for personalization")
    args = parser.parse_args()

    run(args.query, user_name=args.user)


if __name__ == "__main__":
    main()


