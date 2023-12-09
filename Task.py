from dataclasses import dataclass

from AgentRole import AgentRole


@dataclass
class Task:
    for_agent_role: AgentRole
    content: str
    for_agent_name = ""
