import os
import openai


def respond_to_prompt(prompt: str, model: str = "gpt-3.5-turbo") -> str:
    """Send a prompt to OpenAI's ChatCompletion API and return the response.

    If the ``OPENAI_API_KEY`` environment variable is not set, a message is
    returned instead of attempting a network call.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return "OpenAI API key not configured."

    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model=model, messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"].strip()


def run_interactive(model: str = "gpt-3.5-turbo") -> None:
    """Start an interactive chat session."""
    print("Starting AGI CLI (experimental). Type 'exit' to quit.")
    while True:
        try:
            user_input = input("> ")
        except (EOFError, KeyboardInterrupt):
            break
        if user_input.strip().lower() in {"exit", "quit"}:
            break
        reply = respond_to_prompt(user_input, model=model)
        print(reply)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Simple CLI interface using OpenAI's Chat API."
    )
    parser.add_argument("--model", default="gpt-3.5-turbo", help="OpenAI model name")
    args = parser.parse_args()
    run_interactive(args.model)
