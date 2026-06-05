import json


def parse_presentation_response(response: dict):
    if response.get("error"):
        return response

    try:
        return json.loads(response["result"])

    except json.JSONDecodeError:
        return {
            "error": True,
            "message": "LLM returned invalid JSON",
            "raw_response": response.get("result")
        }