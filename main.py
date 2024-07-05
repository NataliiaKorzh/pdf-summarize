import os

from dotenv import load_dotenv
from fastapi import FastAPI

from app import router

app = FastAPI()
load_dotenv()


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


app.include_router(router.router)
