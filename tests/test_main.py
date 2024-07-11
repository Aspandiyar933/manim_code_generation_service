from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_generate_manim_code():
    response = client.post("/generate-manim-code/", json={"description": "A simple animation"})
    assert response.status_code == 200
    assert "manim_code" in response.json()
