from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .generator import generate_manim_code

app = FastAPI()

class Prompt(BaseModel):
    description: str

@app.post("/generate-manim-code/")
async def generate_code(prompt: Prompt):
    try:
        code = await generate_manim_code(prompt.description)
        return {"manim_code": code}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))