from dotenv import load_dotenv
from fastapi import FastAPI

from app.routers.presentation import router

load_dotenv()

app = FastAPI()

app.include_router(router)


@app.get("/")
def root():
    return {
        "message": "AI Developer Roadmap"
    }