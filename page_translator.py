"""
page_translator.py
Description: Handles translation of novel content using OpenAI's API
"""

from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def page_translate(prompt):
    """
    Translates text using OpenAI's API

    Args:
        prompt (str): Text to be translated

    Returns:
        str: Translated text from OpenAI
    """
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": prompt
            }
        ]
    )


    # Access the content attribute directly
    return completion.choices[0].message.content
