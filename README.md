# AI Agent

Minimal interactive AI assistant using LangChain and LangGraph.

Quick start

1. Create a `.env` file in the project root with your OpenAI key:

```
OPENAI_API_KEY=sk-...your key...
OPENAI_MODEL=gpt-4o-mini
```

2. Run the assistant with uv:

```bash
uv run main.py
```

3. Interact in the REPL. Type `quit` to exit.

Notes

- The current `main.py` expects `OPENAI_API_KEY`. To change model, set `OPENAI_MODEL` in `.env`.
- You previously installed `langchain-ollama`. To use Ollama or other providers, update `main.py` to instantiate the appropriate client and provider config.
- If you hit rate/quota errors with OpenAI, consider switching models or providers, or check your billing/limits.

Files

- `main.py`: entrypoint REPL that sends messages to the configured model.

License / Author

Created by Rajan-sharma-0
