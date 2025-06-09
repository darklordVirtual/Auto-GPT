import unittest
from unittest.mock import patch

import tests.context
from autogpt.commands.generate_docs import generate_docs


class TestGenerateDocs(unittest.TestCase):
    @patch("autogpt.commands.generate_docs.call_ai_function")
    def test_generate_docs_calls_ai_function(self, mock_call):
        mock_call.return_value = "Docstring"
        result = generate_docs("print('hello')", focus=["usage"])
        self.assertEqual(result, "Docstring")
        function_string = (
            "def generate_documentation(code: str, focus: Optional[List[str]] = None) -> str:"
        )
        mock_call.assert_called_once_with(
            function_string,
            ["print('hello')", "[\"usage\"]"],
            "Generates documentation for the provided code, focusing on specified areas if required.",
        )


if __name__ == "__main__":
    unittest.main()
