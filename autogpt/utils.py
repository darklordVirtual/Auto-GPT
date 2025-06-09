"""Miscellaneous helper functions used across the project.

Currently this module provides small utilities for reading user input and
validating YAML files used for configuration.
"""

import yaml
from colorama import Fore


def clean_input(prompt: str = ""):
    """Read user input while gracefully handling ``CTRL+C``."""
    try:
        return input(prompt)
    except KeyboardInterrupt:
        print("You interrupted Auto-GPT")
        print("Quitting...")
        exit(0)


def validate_yaml_file(file: str):
    """Validate the given YAML configuration file.

    Returns a tuple ``(success, message)`` describing the result.
    """
    try:
        with open(file, encoding="utf-8") as fp:
            yaml.load(fp.read(), Loader=yaml.FullLoader)
    except FileNotFoundError:
        return (False, f"The file {Fore.CYAN}`{file}`{Fore.RESET} wasn't found")
    except yaml.YAMLError as e:
        return (
            False,
            f"There was an issue while trying to read with your AI Settings file: {e}",
        )

    return (True, f"Successfully validated {Fore.CYAN}`{file}`{Fore.RESET}!")
