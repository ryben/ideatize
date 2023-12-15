from util import Log
from util.FileManager import FileManager
from agency.TalentPool import TalentPool
from tasking.TaskManager import TaskManager


class AgentManager:
    def __init__(self, task_manager: TaskManager, file_manager: FileManager):
        self.task_manager = task_manager
        self.file_manager = file_manager

    def start(self):
        Log.p(f"Tasks: {len(self.task_manager.tasks)}")
        while self.task_manager.has_tasks():
            task = self.task_manager.pop_task()
            agent = TalentPool(self.file_manager).create_agent(task)
            # agent.start()  # TODO("Run async")
