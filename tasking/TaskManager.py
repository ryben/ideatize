from typing import List

from tasking.Task import Task


class TaskManager:
    def __init__(self):
        self.tasks = []

    def push_task(self, task: Task):
        self.tasks.append(task)
        self.sync()

    def pop_task(self) -> Task:
        popped_task = self.tasks.pop()
        self.sync()
        return popped_task

    def has_tasks(self) -> bool:
        return len(self.tasks) > 0

    def sync(self):
        print(self.tasks)
