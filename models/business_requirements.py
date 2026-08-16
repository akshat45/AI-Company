from pydantic import BaseModel


class BusinessRequirements(BaseModel):

    requirements: list[str]

    user_stories: list[str]

    acceptance_criteria: list[str]