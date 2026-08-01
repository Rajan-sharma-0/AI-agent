from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from langchain.tools import tool
import os

@tool
def calculater(a: float, b: float) -> str:
    """Return a short string describing the sum of two numbers."""
    return f"The sum of {a} and {b} is {a+b}"

def main():
    model = ChatOllama(
        model="gemma3:1b",
        temperature=0,
    )

    tools = [calculater]
    agent_executor = create_agent(model, tools)

    print("Hello I am your AI assistant How can I help you")

    while True:
        user_input = input("\nYou: ").strip()

        if user_input == "quit":
            break

        try:
            result = agent_executor.invoke(
                {"messages": [HumanMessage(content=user_input)]}
            )
        except Exception as e:
            msg = str(e)
            if "does not support tools" in msg:
                print("\nNote: selected model does not support tools — retrying without tools.")
                agent_executor = create_agent(model, [])
                result = agent_executor.invoke(
                    {"messages": [HumanMessage(content=user_input)]}
                )
            else:
                raise

        print("\nAssistant:", result["messages"][-1].content)


if __name__ == "__main__":
    main()