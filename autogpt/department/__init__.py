"""Utilities for managing a department of Auto-GPT-powered employees."""

from .department import Department, Employee
from .loader import load_department_from_file

__all__ = ["Department", "Employee", "load_department_from_file"]
