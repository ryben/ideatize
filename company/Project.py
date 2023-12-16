from typing import List

from company.Session import Session
from company.SessionManager import SessionManager
from company.TeamMember import TeamMember
from resource.ResourceManager import ResourceManager
from util import Log


class Project:
    name: str
    sessions: List[Session]

    def __init__(self, name: str, team_members: List[TeamMember]):
        self.name = name
        self.team_members = team_members

    def create_session(self) -> Session:
        Log.p(f"Creating session")

        resource_manager = ResourceManager()
        session_manager = SessionManager(resource_manager, self.team_members)
        return Session(session_manager)
