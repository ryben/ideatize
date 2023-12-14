from resource.Resource import Resource
from tasking.TaskManager import TaskManager


class SessionManager:
    def __init__(self, task_manager: TaskManager):
        self.task_manager = task_manager

    def work(self):
        print(f"Tasks: {len(self.task_manager.tasks)}")
        while self.task_manager.has_tasks():
            task = self.task_manager.pop_task()
            # agent = TalentPool(self.file_manager).create_agent(task)
            # agent.start()  # TODO("Run async")

    def generate_tasks_from_resource(self, resource: Resource):
        for task in self.task_manager.tasks:
            pass


