from fastapi import APIRouter
import json

from app.models.requests import (
    GenerateRequest,
    PresentationRequest
)

from app.models.presentation import PresentationResponse
from app.prompts.presentation_prompt import presentation_prompt
from app.parsers.presentation_parser import parse_presentation_response
from app.services.llm_service import ask_llm
from fastapi.responses import JSONResponse


router = APIRouter()


@router.post("/generate")
def generate(request: GenerateRequest):
    return ask_llm(request.prompt)


@router.post(
    "/presentation",
    response_model=PresentationResponse
)

def presentation(request: PresentationRequest):

    prompt = presentation_prompt.format(
    topic=request.topic,
    audience=request.audience,
    slides=request.slides
)
    response = ask_llm(prompt)

    parsed_response = parse_presentation_response(response)

    if parsed_response.get("error"):
        return JSONResponse(
            status_code=502,
            content=parsed_response
        )

    return parsed_response