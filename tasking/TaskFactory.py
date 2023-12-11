from prompt.Prompt import Prompt
from tasking.Task import Task
from tasking.graph.TaskingGraph import TaskingGraph


class TaskFactory:
    def __init__(self, tasking_graph: TaskingGraph):
        self.tasking_graph = tasking_graph

    def from_source(self, source):
        # TODO("Instantiate task based on Prompt type")
        return Task("ARCHITECT", source.content)

    def create(self, assignee: str, content: str):
        return Task(assignee, content)
