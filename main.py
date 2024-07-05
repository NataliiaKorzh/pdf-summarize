import os

from fastapi import FastAPI, File, UploadFile, HTTPException
import openai
from openai import OpenAI
import PyPDF2
from dotenv import load_dotenv


app = FastAPI()
load_dotenv()


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


@app.post("/summarize")
async def summarize(file: UploadFile = File(...)):
    try:
        if file.content_type != "application/pdf":
            raise HTTPException(status_code=400, detail="Uploaded file must be a PDF")

        pdf_reader = PyPDF2.PdfReader(file.file)
        client = OpenAI(api_key=OPENAI_API_KEY)

        num_pages = len(pdf_reader.pages)
        if num_pages != 1:
            raise HTTPException(status_code=400, detail="PDF file must have exactly one page")

        page = pdf_reader.pages[0]
        text = page.extract_text()

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "The helpful assistant for text summarization."
                },
                {
                    "role": "user",
                    "content": text
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

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
