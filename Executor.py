from FileManager import FileManager
from Project import Project
from agency.AgentManager import AgentManager
from prompt.Prompt import Prompt
from tasking.TaskFactory import TaskFactory
from tasking.TaskManager import TaskManager


class Executor:
    def __init__(self, project: Project):
        self.task_manager = TaskManager()
        self.file_manager = FileManager(project)
        self.agent_manager = AgentManager(self.task_manager, self.file_manager)
        self.task_factory = TaskFactory()

    def start(self, prompt: Prompt = None):
        task = self.task_factory.create("ARCHITECT", prompt.content)
        self.task_manager.push_task(task)

        self.agent_manager.start()
