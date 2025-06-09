"""Simple text classification utilities using scikit-learn.

The TaskClassifier can categorize short task descriptions into pre-
defined labels. It is meant as a minimal example showing how machine
learning can be integrated into Auto-GPT.
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterable, Tuple

import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC


class TaskClassifier:
    """Trainable classifier for short text snippets."""

    def __init__(self, model_path: str | Path | None = None) -> None:
        self.pipeline: Pipeline | None = None
        if model_path:
            self.load(model_path)
        else:
            self.pipeline = Pipeline(
                [
                    ("tfidf", TfidfVectorizer()),
                    ("clf", LinearSVC()),
                ]
            )

    def train(self, data: Iterable[Tuple[str, str]]) -> None:
        """Train the classifier with (text, label) pairs."""
        texts, labels = zip(*data)
        assert self.pipeline is not None
        self.pipeline.fit(texts, labels)

    def predict(self, text: str) -> str:
        """Return a predicted label for ``text``."""
        assert self.pipeline is not None
        return self.pipeline.predict([text])[0]

    def save(self, path: str | Path) -> None:
        """Persist the model to ``path`` using joblib."""
        assert self.pipeline is not None
        joblib.dump(self.pipeline, path)

    def load(self, path: str | Path) -> None:
        """Load a previously saved model from ``path``."""
        self.pipeline = joblib.load(path)
