from agents.base_agent import BaseAgent
from models.business_requirements import BusinessRequirements
from models.technical_solution import TechnicalSolution


class SoftwareDeveloperAgent(BaseAgent):

    def __init__(self):

        super().__init__(
            "prompts/software_developer.txt"
        )

    def develop(
        self,
        requirements: BusinessRequirements
    ) -> TechnicalSolution:

        developer_input = f"""
        Business Requirements:

        Requirements:
        {requirements.requirements}

        User Stories:
        {requirements.user_stories}

        Acceptance Criteria:
        {requirements.acceptance_criteria}
        """

        response = self.client.models.generate_content(
            model=self.model,
            contents=developer_input,
            config={
                "system_instruction": self.system_prompt,
                "response_mime_type": "application/json",
                "response_schema": TechnicalSolution,
            }
        )

        return response.parsed