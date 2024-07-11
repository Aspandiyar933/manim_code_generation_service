import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    def __init__(self) -> None:
        self.llm_api_key = os.getenv("LLM_API_KEY")

