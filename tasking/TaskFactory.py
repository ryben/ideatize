from agency.AgentRole import AgentRole
from prompt.ResearchPrompt import ResearchPrompt
from tasking.Task import Task


class TaskFactory:
    # TODO("Design mapping on a config file")
    @staticmethod
    def from_source(source):
        if isinstance(source, ResearchPrompt):
            return Task(AgentRole.ARCHITECT, source.content)
