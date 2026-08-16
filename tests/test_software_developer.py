from agents.software_developer import SoftwareDeveloperAgent


def test_software_developer():
    developer = SoftwareDeveloperAgent()

    result = developer.run(
        "Build a REST API for managing employees."
    )

    print(result)