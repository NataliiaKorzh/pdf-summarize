import os

from fastapi import FastAPI, File, UploadFile, HTTPException, APIRouter
from dotenv import load_dotenv

from app.services.openai_service import summarize_text
from app.services.pdf_service import extract_text_from_pdf

app = FastAPI()
router = APIRouter()
load_dotenv()


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


@router.post("/summarize")
async def summarize(file: UploadFile = File(...)):

    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Uploaded file must be a PDF")

    try:
        text = extract_text_from_pdf(file)
        if not text:
            raise HTTPException(status_code=400, detail="Could not extract text from PDF")

        summary = await summarize_text(text)

        return {"summary": summary}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
