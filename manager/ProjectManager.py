from manager.SessionManager import SessionManager
from model.Data import Project, Session, Staff, Role
from model.StaffMember import StaffMember
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

        for staff in project.staff:
            self.staff_members.append(StaffMember(staff, roles))

        for session in project.sessions:
            self.session_managers.append(SessionManager(session, self.staff_members))

    def create_session(self) -> Session:
        Log.p(f"Creating session")
        session = Session("1")  # TODO("Make unique IDs")
        self.session_managers.append(SessionManager(session, self.staff_members))
        return session

    def get_session_manager(self, session: Session):
        for session_manager in self.session_managers:
            if session_manager.session == session:
                return session_manager
