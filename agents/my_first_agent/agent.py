from google_adk import Agent, AgentConfig

# Configure the agent to use the IDE's session
config = AgentConfig(
    use_antigravity_session=True,
    api_key=None  # Explicitly ensuring no manual API key is required
)

agent = Agent(
    name="my_first_agent",
    config=config
)

@agent.task
def main_task(context):
    """
    Main entry point for the agent's logic.
    """
    print(f"Agent {agent.name} is running using Antigravity session.")
    return "Ready to serve."

if __name__ == "__main__":
    agent.run()
