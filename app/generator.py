from .llm_client import LLMClient
from .config import Settings

settings = Settings()
llm_client = LLMClient(settings.llm_api_key)

async def generate_manim_code(prompt: str) -> str:
    full_prompt = f'''
        You are a professional teacher who explains math through visualization using Manim. 
        You should create Manim code from the user prompt.
        Please, return your response in the following JSON array format: 
        {
            "manim_code": [
                {
                    "code": "manim code"
                }
            ]
        }
        If the user prompt is irrelevant, return an empty array of code.
    '''
    generated_code = await llm_client.generate_code(full_prompt)
    return generated_code