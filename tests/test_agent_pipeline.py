from agents.business_analyst import BusinessAnalystAgent
from agents.software_developer import SoftwareDeveloperAgent


def test_business_analyst_to_developer():

    user_requirement = """
    Build an employee management system.

    Users should be able to:
    - Create employees
    - View employees
    - Update employees
    - Delete employees

    Each employee should have:
    - ID
    - Name
    - Email
    - Department
    """

    business_analyst = BusinessAnalystAgent()
    developer = SoftwareDeveloperAgent()

    # Step 1: Business Analyst analyzes the requirement
    business_requirements = business_analyst.run(
        user_requirement
    )

    print("\n===== BUSINESS ANALYST =====")
    print(business_requirements)

    # Step 2: Give BA's output to Developer
    developer_input = f"""
    Original User Requirement:
    {user_requirement}

    Business Analyst's Analysis:
    {business_requirements}
    """

    technical_solution = developer.run(
        developer_input
    )

    print("\n===== SOFTWARE DEVELOPER =====")
    print(technical_solution)