from ..agents.react_agent import build_default_react_agent, build_personalized_react_agent
from ..utils.messages import extract_useful_info


def main() -> None:
    agent = build_default_react_agent()
    state = agent.invoke({"messages": [{"role": "user", "content": "what is the weather in sf"}]})
    print(extract_useful_info(state))

    agent_p = build_personalized_react_agent()
    state_p = agent_p.invoke(
        {"messages": [{"role": "user", "content": "what is the weather in sf"}]},
        config={"configurable": {"user_name": "John Smith"}},
    )
    print(extract_useful_info(state_p))


if __name__ == "__main__":
    main()