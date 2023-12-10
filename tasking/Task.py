from dataclasses import dataclass

from agency.AgentRole import AgentRole


@dataclass
class Task:
    for_agent_role: AgentRole
    content: str
    for_agent_name = ""
