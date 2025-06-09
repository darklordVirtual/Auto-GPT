"""Predict the category of a given task description."""

import sys

from autogpt.ml import TaskClassifier

MODEL_PATH = "task_classifier.joblib"


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: predict_task_category.py 'task description'")
        raise SystemExit(1)
    text = sys.argv[1]
    clf = TaskClassifier(MODEL_PATH)
    label = clf.predict(text)
    print(label)


if __name__ == "__main__":
    main()
