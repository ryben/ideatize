from tasking.Task import Task


class TaskFactory:

    def from_source(self, source):
        # TODO("Instantiate task based on Prompt type")
        return Task("ARCHITECT", source.content)

    def create(self, assignee: str, content: str):
        return Task(assignee, content)
