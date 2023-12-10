from FileManager import FileManager
from agency.AgentFactory import AgentFactory
from tasking.TaskManager import TaskManager
from tasking.graph.TaskingGraph import TaskingGraph


class AgentManager:
    def __init__(self, task_manager: TaskManager, tasking_graph: TaskingGraph, file_manager: FileManager):
        self.task_manager = task_manager
        self.tasking_graph = tasking_graph
        self.file_manager = file_manager

    def start(self):
        print(f"Tasks: {len(self.task_manager.tasks)}")
        while self.task_manager.has_tasks():
            task = self.task_manager.pop_task()
            agent = AgentFactory(self.file_manager).create_agent(task)
            agent.start()  # TODO("Run async")
