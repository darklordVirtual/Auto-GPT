"""Computer environment implementations for CUA."""

from .computer import Computer
from .local_playwright import LocalPlaywrightBrowser

# Mapping of supported computer environments used by the CLI
computers_config = {"local-playwright": LocalPlaywrightBrowser}

__all__ = ["Computer", "LocalPlaywrightBrowser", "computers_config"]
