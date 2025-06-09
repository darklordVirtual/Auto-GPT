from __future__ import annotations

import json

from autogpt.llm_utils import call_ai_function


def generate_docs(code: str, focus: list[str] | None = None) -> str:
    """Generate documentation for the provided code."""

    function_string = (
        "def generate_documentation(code: str, focus: Optional[List[str]] = None) -> str:"
    )
    args = [code, json.dumps(focus) if focus is not None else "None"]
    description_string = (
        "Generates documentation for the provided code, focusing on specified areas if required."
    )

    return call_ai_function(function_string, args, description_string)
