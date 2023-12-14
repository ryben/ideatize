from typing import List

from company.SessionManager import SessionManager
from company.TeamMember import TeamMember
from resource.ResourceManager import ResourceManager
from tasking.TaskManager import TaskManager


class Session:
    task_manager: TaskManager
    session_manager: SessionManager
    resource_manager: ResourceManager

    def __init__(self, task_manager: TaskManager,
                 session_manager: SessionManager,
                 resource_manager: ResourceManager,
                 team_members: List[TeamMember]):
        self.task_manager = task_manager
        self.session_manager = session_manager
        self.resource_manager = resource_manager
        self.team_members = team_members

    def assemble_team_members(self) -> List[TeamMember]:
        pass
