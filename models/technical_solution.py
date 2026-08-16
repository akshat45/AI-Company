from pydantic import BaseModel


class TechnicalSolution(BaseModel):

    architecture: str

    technologies: list[str]

    project_structure: list[str]

    implementation_plan: list[str]

    risks: list[str]