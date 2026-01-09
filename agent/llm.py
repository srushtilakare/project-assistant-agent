def get_plan_from_llm(goal):
    """
    Temporary mocked LLM response.
    Later we replace this with real OpenAI API.
    """
    return [
        "Understand the problem requirements",
        "Break project into major components",
        "Design solution architecture",
        "Implement core functionality",
        "Test and refine the system"
    ]
