"""Computer environment implementations for CUA."""

from .computer import Computer
from .local_playwright import LocalPlaywrightBrowser

__all__ = ["Computer", "LocalPlaywrightBrowser"]
