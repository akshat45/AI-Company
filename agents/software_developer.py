from agents.base_agent import BaseAgent
from models.business_requirements import BusinessRequirements
from tools.file_tools import (
    list_files,
    read_file,
    write_file,
)


class SoftwareDeveloperAgent(BaseAgent):

    def __init__(self):

        super().__init__(
            "prompts/software_developer.txt"
        )

    def work(
        self,
        requirements: BusinessRequirements
    ) -> str:

        developer_input = f"""
        You are working as a software developer.

        You have access to the project workspace.

        Your task is to inspect the existing project and
        implement the requested functionality.

        Business Requirements:

        Requirements:
        {requirements.requirements}

        User Stories:
        {requirements.user_stories}

        Acceptance Criteria:
        {requirements.acceptance_criteria}

        Before making changes:
        1. Inspect the existing project.
        2. Read relevant files.
        3. Understand the existing architecture.
        4. Implement the required changes.
        5. Verify your work.

        Use the available tools whenever necessary.
        """

        response = self.client.models.generate_content(
            model=self.model,
            contents=developer_input,
            config={
                "system_instruction": self.system_prompt,
                "tools": [
                    list_files,
                    read_file,
                    write_file,
                ],
            },
        )

        return response.text