"""Example script for training a simple task classifier."""

from autogpt.ml import TaskClassifier

SAMPLE_DATA = [
    ("Implement new API endpoint", "coding"),
    ("Refactor legacy code", "coding"),
    ("Write user documentation", "documentation"),
    ("Update README with latest instructions", "documentation"),
    ("Create unit tests for models", "testing"),
    ("Run integration tests", "testing"),
]


def main() -> None:
    classifier = TaskClassifier()
    classifier.train(SAMPLE_DATA)
    classifier.save("task_classifier.joblib")
    print("Model saved to task_classifier.joblib")


if __name__ == "__main__":
    main()
