class AgentMemory:
    """
    Manages the internal state of an AI agent, including its objectives,
    the roadmap to achieve them, and a record of past events.
    """
    
    def __init__(self):
        # The high-level objective the agent is trying to accomplish
        self.goal = None
        
        # A list of specific tasks/actions (the "roadmap")
        self.plan = []
        
        # Tracks the current position within the plan list
        self.current_step = 0
        
        # A log of all previous actions, observations, or thoughts
        self.history = []

    def set_goal(self, goal: str):
        """Assigns a new high-level objective to the agent."""
        self.goal = goal

    def set_plan(self, plan: list):
        """
        Stores a new sequence of steps. 
        Resets the counter to 0 so the agent starts from the beginning.
        """
        self.plan = plan
        self.current_step = 0

    def add_history(self, entry: str):
        """Appends a record of a recent action or event to the agent's log."""
        self.history.append(entry)

    def get_next_step(self):
        """
        Retrieves the current task from the plan and moves the pointer forward.
        Returns None if the plan is finished or empty.
        """
        # Ensure we haven't reached the end of the step list
        if self.current_step < len(self.plan):
            # Fetch the step at the current index
            step = self.plan[self.current_step]
            # Increment the index so the next call gets the next step
            self.current_step += 1
            return step
        
        # Return None if no steps are left to execute
        return None