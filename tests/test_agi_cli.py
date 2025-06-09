from autogpt.agi_cli import respond_to_prompt

def test_respond_to_prompt_no_api_key(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    assert "API key" in respond_to_prompt("Hello")


def test_respond_to_prompt_with_mock(monkeypatch):
    def mock_create(model, messages):
        return {"choices": [{"message": {"content": "Hi"}}]}

    monkeypatch.setenv("OPENAI_API_KEY", "test")
    monkeypatch.setattr("openai.ChatCompletion.create", mock_create)
    assert respond_to_prompt("Hello") == "Hi"
