from agency.Agent import Agent
from tasking.Task import Task


class TalentPool:

    def __init__(self):
        pass

    @staticmethod
    def create_agent(task: Task) -> Agent:
        # TODO("Instantiate agent based on which one the task is for")
        return Agent(task.assignee, "Research about current trends in Philippines", [], "Researcher")
