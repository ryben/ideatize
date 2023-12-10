from FileManager import FileManager
from agency.Agent import Agent
from tasking.Task import Task


class AgentFactory:

    def __init__(self, file_manager: FileManager):
        self.file_manager = file_manager
        self.agent_definitions = {}

    @staticmethod
    def create_agent(task: Task) -> Agent:
        # TODO("Instantiate agent based on which one the task is for")
        return Agent(task.assignee, "Research about current trends in Philippines", [], "Researcher")

    def load_agent(self):
        self.agent_definitions = self.file_manager.load_agents()