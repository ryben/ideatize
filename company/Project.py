from dataclasses import dataclass
from typing import List


from agency.TalentPool import TalentPool
from company.Session import Session
from company.SessionManager import SessionManager
from company.TeamMember import TeamMember
from resource.ResourceManager import ResourceManager
from tasking.TaskManager import TaskManager


@dataclass
class Project:
    name: str
    sessions: List[Session]
    talentPool: TalentPool

    def __init__(self, name: str, team_members: List[TeamMember]):
        self.name = name
        self.team_members = team_members

    def create_session(self) -> Session:
        task_manager = TaskManager()
        return Session(task_manager, SessionManager(task_manager), ResourceManager())
