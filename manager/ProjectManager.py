import copy

from manager.SessionManager import SessionManager
from model.Data import Project, Session, Role
from staff.StaffMember import StaffMember
from util import Log


class ProjectManager:
    project: Project
    roles: list[Role]
    staff_members: list[StaffMember]
    session_managers: list[SessionManager]

    def __init__(self, project: Project, roles: list[Role]):
        self.project = project
        self.roles = roles
        self.staff_members = []
        self.session_managers = []

        for session in project.sessions:
            self.add_session_manager(session)

    def find_role_by_name(self, role_name) -> Role:
        for role in self.roles:
            if role.name == role_name:
                return role

    def add_session_manager(self, session: Session):
        self.session_managers.append(SessionManager(session, self.project.staff, self.roles))

    def create_session(self) -> Session:
        Log.p(f"Creating session")
        session = Session("1")  # TODO("Make unique IDs")
        self.add_session_manager(session)
        return session

    def get_session_manager(self, session: Session):
        for session_manager in self.session_managers:
            if session_manager.session == session:
                return session_manager
