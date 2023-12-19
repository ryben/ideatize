from manager.SessionManager import SessionManager
from model.Data import Project, Session
from util import Log


class ProjectManager:
    project: Project
    session_managers: list[SessionManager]

    def __init__(self, project):
        self.project = project
        self.session_managers = []
        for session in project.sessions:
            self.session_managers.append(SessionManager(session))

    def create_session(self) -> Session:
        Log.p(f"Creating session")
        session = Session("1")  # TODO("Make unique IDs")
        self.session_managers.append(SessionManager(session))
        return session

    def get_session_manager(self, session: Session):
        for session_manager in self.session_managers:
            if session_manager.session  == session:
                return session_manager

