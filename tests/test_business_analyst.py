from agents.business_analyst import BusinessAnalystAgent


def test_business_analyst_structured_output():

    analyst = BusinessAnalystAgent()

    result = analyst.analyze(
        """
        Build an employee management system.

        Users should be able to create, view,
        update and delete employees.

        Each employee has a name, email and department.
        """
    )

    print("\n===== STRUCTURED BA OUTPUT =====")
    print(result)

    print("\nRequirements:")
    print(result.requirements)

    print("\nUser Stories:")
    print(result.user_stories)

    print("\nAcceptance Criteria:")
    print(result.acceptance_criteria)