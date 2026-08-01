from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama


def main() -> None:
    model = ChatOllama(
        model="gemma3:1b",
        temperature=0,
    )

    tools = []
    agent_executor = create_agent(model, tools)

    print("Hello I am your AI assistant How can I help you")

    while True:
        user_input = input("\nYou: ").strip()

        if user_input == "quit":
            break

        result = agent_executor.invoke(
            {"messages": [HumanMessage(content=user_input)]}
        )
        print("\nAssistant:", result["messages"][-1].content)


if __name__ == "__main__":
    main()