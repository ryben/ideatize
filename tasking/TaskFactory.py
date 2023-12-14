from tasking.Task import Task
from tasking.TaskStatus import TaskStatus


class TaskFactory:
    @staticmethod
    def fromPrompt(prompt) -> Task:
        task = Task()
        task.status = TaskStatus.READY
        return task
