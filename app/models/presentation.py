from pydantic import BaseModel

class Slide(BaseModel):
    title: str
    description: str