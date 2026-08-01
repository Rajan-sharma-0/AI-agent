from __future__ import annotations

import os

from dotenv import load_dotenv
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent


load_dotenv()


@tool
def get_time() -> str:
    """Return a simple status string for the agent."""
    return "I am ready to use the Grok API."


def main() -> None:
    model = ChatOpenAI(
        model=os.getenv("GROK_MODEL", "grok-4"),
        api_key=os.getenv("GROK_API_KEY"),
        base_url="https://api.x.ai/v1",
    )
    agent = create_react_agent(model, tools=[get_time])
    result = agent.invoke(
        {"messages": [HumanMessage(content="Say hello in one short sentence.")]}
    )
    print(result["messages"][-1].content)
