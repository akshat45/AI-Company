from pathlib import Path

from google import genai

from config.settings import settings

class BaseAgent:

    def __init__(self, prompt_file: str):

        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

        self.model = settings.MODEL

        base_dir = Path(__file__).resolve().parent.parent
        prompt_path = base_dir / prompt_file

        self.system_prompt = prompt_path.read_text(
            encoding="utf-8"
        )

    def run(self, user_input: str) -> str:

        response = self.client.models.generate_content(
            model=self.model,
            contents=user_input,
            config={
                "system_instruction": self.system_prompt
            }
        )

        return response.text

  