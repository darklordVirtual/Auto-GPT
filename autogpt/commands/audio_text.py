"""Utilities for converting speech audio to text via HuggingFace.

The functions in this module send audio data to the HuggingFace inference
API and return a plain text transcription. A HuggingFace API token and model
identifier must be configured in ``Config``.
"""

import requests
import json

from autogpt.config import Config
from autogpt.workspace import path_in_workspace

cfg = Config()


def read_audio_from_file(audio_path: str) -> str:
    """Return a transcription of the audio file at ``audio_path``.

    Parameters
    ----------
    audio_path : str
        Path to the audio file inside the workspace.

    Returns
    -------
    str
        The text obtained from the speech in ``audio_path``.
    """
    audio_path = path_in_workspace(audio_path)
    with open(audio_path, "rb") as audio_file:
        audio = audio_file.read()
    return read_audio(audio)


def read_audio(audio: bytes) -> str:
    """Send raw ``audio`` bytes to the HuggingFace API and return text.

    Parameters
    ----------
    audio : bytes
        Raw audio data to be transcribed.

    Returns
    -------
    str
        Text transcription of the provided audio.
    """
    model = cfg.huggingface_audio_to_text_model
    api_url = f"https://api-inference.huggingface.co/models/{model}"
    api_token = cfg.huggingface_api_token
    headers = {"Authorization": f"Bearer {api_token}"}

    if api_token is None:
        raise ValueError(
            "You need to set your Hugging Face API token in the config file."
        )

    response = requests.post(
        api_url,
        headers=headers,
        data=audio,
    )

    text = json.loads(response.content.decode("utf-8"))["text"]
    return "The audio says: " + text
