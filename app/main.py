from dotenv import load_dotenv
from fastapi import FastAPI

from app.routers.presentation import router as presentation_router
from app.routers.rag import router as rag_router

load_dotenv()

app = FastAPI()

app.include_router(presentation_router)
app.include_router(rag_router)


@app.get("/")
def root():
    return {
        "message": "AI Developer Roadmap"
    }