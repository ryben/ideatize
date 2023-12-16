from typing import List

from agency.TalentPool import TalentPool
from company.Session import Session
from company.SessionManager import SessionManager
from company.TeamMember import TeamMember
from resource.ResourceManager import ResourceManager
from tasking.TaskManager import TaskManager
from util import Log


class Project:
    name: str
    sessions: List[Session]
    talentPool: TalentPool

    def __init__(self, name: str, team_members: List[TeamMember]):
        self.name = name
        self.team_members = team_members

    def create_session(self) -> Session:
        Log.p(f"Creating session")

        task_manager = TaskManager()
        resource_manager = ResourceManager()
        session_manager = SessionManager(resource_manager, task_manager, self.team_members)
        return Session(session_manager)
