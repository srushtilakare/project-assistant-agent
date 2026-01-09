from agent.controller import AgentController

def main():
    print("=== Project Assistant AI Agent ===")
    goal = input("Enter your project goal: ")

    agent = AgentController()
    agent.start(goal)

    while True:
        user_input = input("\nProceed to next step? (yes/no): ").lower()
        if user_input == "yes":
            agent.next_step()
        else:
            print("\n[Agent] Waiting for your decision.")
            break


if __name__ == "__main__":
    main()
