from agents.base_agent import BaseAgent
from models.business_requirements import BusinessRequirements


class BusinessAnalystAgent(BaseAgent):

    def __init__(self):

        super().__init__(
            "prompts/business_analyst.txt"
        )

    def analyze(self, user_input: str) -> BusinessRequirements:

        response = self.client.models.generate_content(
            model=self.model,
            contents=user_input,
            config={
                "system_instruction": self.system_prompt,
                "response_mime_type": "application/json",
                "response_schema": BusinessRequirements,
            }
        )

        return response.parsed