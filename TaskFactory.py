from AgentRole import AgentRole
from ResearchPrompt import ResearchPrompt
from Task import Task


class TaskFactory:

    @staticmethod
    def from_source(source):
        if isinstance(source, ResearchPrompt):
            return Task(AgentRole.RESEARCHER, source.content)
        elif isinstance(source, AgentRole):
            agent_role = AgentRole(source)
            if agent_role == AgentRole.ARCHITECT:
                pass
