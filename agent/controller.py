from agent.memory import AgentMemory
from agent.llm import get_plan_from_llm

class AgentController:
    """
    The Orchestrator class that manages the agent's lifecycle:
    receiving goals, generating plans via LLM, and executing steps.
    """
    
    def __init__(self):
        # Initialize the memory module to track goals, plans, and history
        self.memory = AgentMemory()

    def start(self, goal: str):
        """
        Initializes the agent with a specific objective.
        1. Saves the goal to memory.
        2. Calls the LLM to break the goal into actionable steps.
        3. Stores the resulting plan.
        """
        print("\n[Agent] Received goal:")
        print(f"→ {goal}")

        # Store the high-level objective in memory
        self.memory.set_goal(goal)

        print("\n[Agent] Thinking and creating a plan...")
        
        # Request the LLM to generate a list of steps based on the goal
        plan = get_plan_from_llm(goal)

        # Save the generated plan into memory for sequential execution
        self.memory.set_plan(plan)

        # Visual feedback for the user to see what the agent intends to do
        print("\n[Agent] Proposed Plan:")
        for idx, step in enumerate(plan, start=1):
            print(f"{idx}. {step}")

        return plan

    def next_step(self):
        """
        Advances the agent to the next task in its stored plan.
        If no steps remain, it signals that the goal is finished.
        """
        # Ask memory for the next pending step and increment the counter
        step = self.memory.get_next_step()
        
        if step:
            # Plan is still in progress
            print(f"\n[Agent] Next recommended step:")
            print(f"→ {step}")
        else:
            # Memory returned None because current_step reached the end of the list
            print("\n[Agent] Goal completed 🎉")