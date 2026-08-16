from agents.business_analyst import BusinessAnalystAgent
from agents.software_developer import SoftwareDeveloperAgent


def main():

    print("=" * 60)
    print("AI Software Company")
    print("=" * 60)

    project = input("\nDescribe your software idea:\n\n> ")

    # Business Analyst
    analyst = BusinessAnalystAgent()

    requirements = analyst.analyze(project)

    print("\n")
    print("=" * 60)
    print("Business Analyst Report")
    print("=" * 60)

    print("\nRequirements:")
    for requirement in requirements.requirements:
        print(f"- {requirement}")

    print("\nUser Stories:")
    for story in requirements.user_stories:
        print(f"- {story}")

    print("\nAcceptance Criteria:")
    for criteria in requirements.acceptance_criteria:
        print(f"- {criteria}")

    # Software Developer
    developer = SoftwareDeveloperAgent()

    result = developer.work(requirements)

    print("\n")
    print("=" * 60)
    print("Software Developer Report")
    print("=" * 60)

    print(result)


if __name__ == "__main__":
    main()