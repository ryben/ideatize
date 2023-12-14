from dataclasses import dataclass
from typing import List

from agency.TalentPool import TalentPool
from company.Repository import Repository
from company.SessionManager import SessionManager
from company.Session import Session
from company.TaskManager import TaskManager
from company.TeamMember import TeamMember


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
        return Session(task_manager, SessionManager(task_manager), Repository())
