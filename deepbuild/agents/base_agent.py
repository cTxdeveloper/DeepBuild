from crewai import Agent
from deepbuild.config.settings import settings


class BaseDeepAgent:
    def __init__(self, role: str, goal: str, backstory: str):
        self.agent = Agent(
            role=role,
            goal=goal,
            backstory=backstory,
            verbose=True,
            allow_delegation=True,
            llm=settings.default_model
        )

    def get_agent(self):
        return self.agent
