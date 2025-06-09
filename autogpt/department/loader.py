"""Helpers for loading department configurations from YAML files."""

import yaml
from .department import Department, Employee


def load_department_from_file(file_path: str) -> Department:
    """Return a :class:`Department` parsed from ``file_path``."""
    with open(file_path, "r", encoding="utf-8") as fp:
        data = yaml.safe_load(fp)

    employees = [
        Employee(name=e.get("name"), role=e.get("role"), goals=e.get("goals", []))
        for e in data.get("employees", [])
    ]
    return Department(name=data.get("name", "Department"), employees=employees)
