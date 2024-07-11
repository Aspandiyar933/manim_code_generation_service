import openai

class LLMClient:
    def __init__(self, api_key:str) -> None:
        self.api_key = api_key
        openai.api_key = self.api_key

    async def generate_code(self, prompt: str) -> str:
        response = openai.Completion.create(
            engine="gpt-4o",
            prompt=prompt,
            max_tokens=500,
            n=1,
            stop=None,
            temperature=0.7
        )
        return response.choices[0].text.strip()
