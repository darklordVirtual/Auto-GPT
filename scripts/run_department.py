"""Run a department of Auto-GPT powered employees from a YAML config."""

import argparse
from autogpt.department import load_department_from_file


def main():
    parser = argparse.ArgumentParser(description="Run a department of agents")
    parser.add_argument(
        "--config",
        default="department_template.yaml",
        help="Path to department YAML config",
    )
    args = parser.parse_args()

    department = load_department_from_file(args.config)
    department.run_all()


if __name__ == "__main__":
    main()
