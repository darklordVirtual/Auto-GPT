"""Machine learning utilities for Auto-GPT.

This package provides simple ML models that can be used to enhance
Auto-GPT with task classification and other features.
"""

from .task_classifier import TaskClassifier

__all__ = ["TaskClassifier"]
