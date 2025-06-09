import unittest
from unittest.mock import patch, MagicMock

from autogpt.commands.codex_integration import generate_code_via_codex, execute_codex_prompt


class TestCodexIntegration(unittest.TestCase):
    def test_generate_code_via_codex(self):
        with patch("openai.Completion.create") as mock_create:
            mock_create.return_value = MagicMock(choices=[MagicMock(text="print('hi')")])
            code = generate_code_via_codex("say hi")
            self.assertEqual(code, "print('hi')")

    def test_execute_codex_prompt(self):
        with patch("openai.Completion.create") as mock_create, patch(
            "autogpt.commands.codex_integration.execute_python_file"
        ) as mock_exec:
            mock_create.return_value = MagicMock(choices=[MagicMock(text="print('test')")])
            mock_exec.return_value = "ok"
            output = execute_codex_prompt("test prompt", file_name="tmp.py")
            self.assertEqual(output, "ok")
            mock_exec.assert_called_once_with("tmp.py")


if __name__ == "__main__":
    unittest.main()
