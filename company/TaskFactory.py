from company.Task import Task


class TaskFactory:
    def __init__(self):
        pass

    @staticmethod
    def fromPrompt(prompt) -> Task:
        task = Task()
        return task
