"""Functions for counting the number of tokens in a message or string."""
from __future__ import annotations

import os
import re

try:
    import tiktoken
except Exception:  # pragma: no cover - tiktoken may not be installed
    tiktoken = None

from autogpt.logs import logger


def _approximate_token_count(text: str) -> int:
    words = re.findall(r"\w+", text)
    return 2 * len(words)


def count_message_tokens(
    messages: list[dict[str, str]], model: str = "gpt-3.5-turbo-0301"
) -> int:
    """
    Returns the number of tokens used by a list of messages.

    Args:
        messages (list): A list of messages, each of which is a dictionary
            containing the role and content of the message.
        model (str): The name of the model to use for tokenization.
            Defaults to "gpt-3.5-turbo-0301".

    Returns:
        int: The number of tokens used by the list of messages.
    """
    encoding = None
    if tiktoken is not None:
        try:
            encoding = tiktoken.encoding_for_model(model)
        except Exception:  # pragma: no cover
            logger.warn("tiktoken unavailable, using approximate token count")
    if model == "gpt-3.5-turbo":
        # !Note: gpt-3.5-turbo may change over time.
        # Returning num tokens assuming gpt-3.5-turbo-0301.")
        return count_message_tokens(messages, model="gpt-3.5-turbo-0301")
    elif model == "gpt-4":
        # !Note: gpt-4 may change over time. Returning num tokens assuming gpt-4-0314.")
        return count_message_tokens(messages, model="gpt-4-0314")
    elif model == "gpt-3.5-turbo-0301":
        tokens_per_message = (
            4  # every message follows <|start|>{role/name}\n{content}<|end|>\n
        )
        tokens_per_name = -1  # if there's a name, the role is omitted
    elif model == "gpt-4-0314":
        tokens_per_message = 3
        tokens_per_name = 1
    else:
        raise NotImplementedError(
            f"num_tokens_from_messages() is not implemented for model {model}.\n"
            " See https://github.com/openai/openai-python/blob/main/chatml.md for"
            " information on how messages are converted to tokens."
        )
    num_tokens = 0
    for message in messages:
        num_tokens += tokens_per_message
        for key, value in message.items():
            if key == "role":
                continue
            if key == "name":
                token_length = 1 if encoding is None else len(encoding.encode(value))
                num_tokens += token_length + tokens_per_name
            else:
                if encoding is not None:
                    num_tokens += len(encoding.encode(value))
                else:
                    num_tokens += _approximate_token_count(value)
    num_tokens += 3  # every reply is primed with <|start|>assistant<|message|>
    return num_tokens


def count_string_tokens(string: str, model_name: str) -> int:
    """
    Returns the number of tokens in a text string.

    Args:
        string (str): The text string.
        model_name (str): The name of the encoding to use. (e.g., "gpt-3.5-turbo")

    Returns:
        int: The number of tokens in the text string.
    """
    if tiktoken is not None:
        try:
            encoding = tiktoken.encoding_for_model(model_name)
            return len(encoding.encode(string))
        except Exception:  # pragma: no cover
            logger.warn("tiktoken unavailable, using approximate token count")
    return _approximate_token_count(string)
