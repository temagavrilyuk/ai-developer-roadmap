from typing import List
from pydantic import BaseModel


class Slide(BaseModel):
    title: str
    description: str


class PresentationResponse(BaseModel):
    slides: List[Slide]