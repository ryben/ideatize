from company.SessionManager import SessionManager
from resource.ResourceManager import ResourceManager
from tasking.TaskManager import TaskManager


class Session:
    task_manager: TaskManager
    session_manager: SessionManager
    resource_manager: ResourceManager

    def __init__(self, task_manager: TaskManager, session_manager: SessionManager, resource_manager: ResourceManager):
        self.task_manager = task_manager
        self.session_manager = session_manager
        self.resource_manager = resource_manager
