from pydantic import BaseModel

class GenerateRequest(BaseModel):
    prompt: str

class PresentationRequest(BaseModel):
    topic: str
    audience: str
    slides: int