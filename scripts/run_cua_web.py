"""Flask web interface for the Computer Using Agent demo."""

import atexit
from flask import Flask, request, render_template_string
from autogpt.cua import Agent, LocalPlaywrightBrowser

app = Flask(__name__)
computer = LocalPlaywrightBrowser(headless=True)
agent = None
conversation = []

PAGE_TEMPLATE = """
<!doctype html>
<title>CUA Web Interface</title>
<h1>Computer Using Agent</h1>
<form method="post">
  <input name="message" autofocus />
  <button type="submit">Send</button>
</form>
{% for item in conversation %}
  <pre>{{ item }}</pre>
{% endfor %}
{% for img in images %}
  <img src="{{ img }}" style="max-width:100%;" />
{% endfor %}
"""

@app.before_first_request
def setup() -> None:
    """Initialize the agent and underlying computer once at startup."""
    global agent
    computer.__enter__()
    agent = Agent(computer=computer, acknowledge_safety_check_callback=lambda m: True)

@app.route("/", methods=["GET", "POST"])
def index():
    """Handle user prompts and display agent output."""
    global conversation
    images = []
    if request.method == "POST":
        message = request.form.get("message", "")
        conversation.append({"role": "user", "content": message})
        outputs = agent.run_full_turn(conversation, print_steps=False)
        conversation.extend(outputs)
        for item in outputs:
            if item.get("output", {}).get("image_url"):
                images.append(item["output"]["image_url"])
    return render_template_string(PAGE_TEMPLATE, conversation=conversation, images=images)

@atexit.register
def cleanup() -> None:
    """Ensure the Playwright browser is closed on shutdown."""
    computer.__exit__(None, None, None)

if __name__ == "__main__":
    app.run(debug=True)
