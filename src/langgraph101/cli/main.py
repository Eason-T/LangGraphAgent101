from __future__ import annotations

import argparse
from typing import Optional

from ..agents.react_agent import (
    build_default_react_agent,
    build_personalized_react_agent,
)
from ..utils.messages import extract_useful_info


def run(query: str, user_name: Optional[str] = None) -> None:
    sf_response = None
    ny_response = None

    if user_name:
        agent = build_personalized_react_agent()
        state = agent.invoke(
            {"messages": [{"role": "user", "content": query}]},
            config={"configurable": {"user_name": user_name}},
        )
    else:
        agent = build_default_react_agent()
        config = {"configurable": {"thread_id": "1"}}
        state = agent.invoke({"messages": [{"role": "user", "content": query}]}, config)
        sf_response = agent.invoke(
            {"messages": [{"role": "user", "content": "what is the weather in sf"}]},
            config,
        )
        ny_response = agent.invoke(
            {"messages": [{"role": "user", "content": "what about new york?"}]}, 
            config,
        )

    summary = extract_useful_info(state)
    # print(state.get("messages", [])[-1].content)
    print(summary["final_text"])
    if sf_response is not None:
        print(sf_response)
    if ny_response is not None:
        print(ny_response)


def main() -> None:
    parser = argparse.ArgumentParser(description="LangGraph101 CLI")
    parser.add_argument("query", type=str, help="User query")
    parser.add_argument(
        "--user",
        dest="user",
        type=str,
        default=None,
        help="User name for personalization",
    )
    args = parser.parse_args()

    run(args.query, user_name=args.user)


if __name__ == "__main__":
    main()
