import PyPDF2
from fastapi import HTTPException


def extract_text_from_pdf(file) -> str:

    pdf_reader = PyPDF2.PdfReader(file.file)

    num_pages = len(pdf_reader.pages)
    if num_pages != 1:
        raise HTTPException(status_code=400, detail="PDF file must have exactly one page")

    page = pdf_reader.pages[0]
    text = page.extract_text()

    return text
