import os

import openai
from dotenv import load_dotenv
from fastapi import HTTPException
from openai import OpenAI

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


async def summarize_text(text: str):
    try:
        client = OpenAI(api_key=OPENAI_API_KEY)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant for text summarization."
                },
                {
                    "role": "user",
                    "content": "Please summarize the following text in a concise and informative manner:\n\n" + text
                }
            ]

        )

        summary = response.choices[0].text.strip()

        return {"summary": summary}

    except openai.AuthenticationError:
        raise HTTPException(status_code=401, detail="Authentication error. Please check your API key.")

    except openai.APIConnectionError:
        raise HTTPException(status_code=503, detail="Connection error. Please try again later.")

    except openai.RateLimitError:
        raise HTTPException(status_code=429, detail="Rate limit exceeded. Please try again later.")
