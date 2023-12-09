from typing import List

from Task import Task


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: Task):
        self.tasks.append(task)
        self.sync()

    def get_task(self, task):
        # TODO("Get task by applicable type")
        self.sync()

    def sync(self):
        print(self.tasks)
