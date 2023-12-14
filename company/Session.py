from company.Repository import Repository
from company.SessionManager import SessionManager
from company.TaskManager import TaskManager


class Session:
    task_manager: TaskManager
    session_manager: SessionManager
    repository: Repository

    def __init__(self, task_manager: TaskManager, session_manager: SessionManager, repository: Repository):
        self.task_manager = task_manager
        self.session_manager = session_manager
        self.repository = repository
