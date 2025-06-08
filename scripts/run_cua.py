"""Example script to run Auto-GPT with CUA using a local browser.

This script relies on code adapted from the `openai-cua-sample-app` project
(MIT licensed) which demonstrates the Computer Using Agent preview.
"""

from autogpt.cua import Agent, LocalPlaywrightBrowser


def main():
    with LocalPlaywrightBrowser() as computer:
        agent = Agent(computer=computer)
        items = []
        while True:
            try:
                user_input = input("> ")
            except EOFError:
                break
            if user_input.lower() == "exit":
                break
            items.append({"role": "user", "content": user_input})
            output_items = agent.run_full_turn(items, print_steps=True)
            items += output_items


if __name__ == "__main__":
    main()
