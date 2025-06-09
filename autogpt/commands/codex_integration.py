"""Integration utilities for OpenAI Codex."""
from __future__ import annotations

import openai

from autogpt.config import Config
from autogpt.commands.execute_code import execute_python_file
from autogpt.workspace import path_in_workspace

CFG = Config()


def generate_code_via_codex(prompt: str, max_tokens: int = 200) -> str:
    """Generate Python code from a natural language prompt using Codex."""
    response = openai.Completion.create(
        engine=CFG.codex_model,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=0,
    )
    return response.choices[0].text


def execute_codex_prompt(prompt: str, file_name: str = "codex_generated.py") -> str:
    """Generate code via Codex from a prompt and execute it."""
    code = generate_code_via_codex(prompt)
    file_path = path_in_workspace(file_name)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(code)
    return execute_python_file(file_name)
