import pytest
from app.generator import generate_manim_code

@pytest.mark.asyncio
async def test_generate_manim_code():
    prompt = "A simple animation"
    code = await generate_manim_code(prompt)
    assert isinstance(code, str)
    assert len(code) > 0
