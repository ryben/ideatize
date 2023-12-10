from agency.Agent import Agent
from agency.AgentRole import AgentRole
from tasking.TaskManager import TaskManager
from tasking.graph.TaskingGraph import TaskingGraph


class AgentManager:
    def __init__(self, task_manager: TaskManager, tasking_graph: TaskingGraph):
        self.task_manager = task_manager
        self.tasking_graph = tasking_graph

    def start(self):
        while self.task_manager.has_tasks():
            task = self.task_manager.pop_task()
            agent = self.create_agent(task)
            agent.start()  # TODO("Run async")

    def create_agent(self, task) -> Agent:
        # TODO("Instantiate agent based on which one the task is for")
        if task.for_agent_role == AgentRole.ARCHITECT:
            # Stub
            return Agent(task.for_agent_role, "Research about current trends in Philippines", [], "Researcher")
