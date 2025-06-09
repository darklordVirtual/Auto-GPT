"""Command-line interface for experimenting with the Computer Using Agent."""

import argparse
from autogpt.cua import Agent
from autogpt.cua.computers import computers_config


def acknowledge_safety_check_callback(message: str) -> bool:
    """Prompt the user to acknowledge a safety warning."""
    response = input(
        f"Safety Check Warning: {message}\nDo you want to acknowledge and proceed? (y/n): "
    ).lower()
    return response.strip() == "y"


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the CUA demo")
    parser.add_argument(
        "--computer",
        choices=computers_config.keys(),
        default="local-playwright",
        help="Computer environment to use",
    )
    parser.add_argument(
        "--input",
        type=str,
        default=None,
        help="Initial user input. If omitted, you will be prompted",
    )
    parser.add_argument("--debug", action="store_true", help="Enable debug output")
    parser.add_argument("--show", action="store_true", help="Display screenshots")
    parser.add_argument(
        "--start-url",
        type=str,
        default="https://bing.com",
        help="Initial URL when using a browser environment",
    )
    args = parser.parse_args()

    ComputerClass = computers_config[args.computer]

    with ComputerClass() as computer:
        agent = Agent(computer=computer, acknowledge_safety_check_callback=acknowledge_safety_check_callback)
        items = []

        if computer.get_environment() == "browser":
            start = args.start_url
            if not start.startswith("http"):
                start = "https://" + start
            computer.goto(start)

        while True:
            try:
                user_input = args.input or input("> ")
                if user_input.lower() == "exit":
                    break
            except EOFError:
                break
            items.append({"role": "user", "content": user_input})
            output_items = agent.run_full_turn(
                items,
                print_steps=True,
                show_images=args.show,
                debug=args.debug,
            )
            items += output_items
            args.input = None


if __name__ == "__main__":
    main()
