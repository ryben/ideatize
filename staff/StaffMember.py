from core.ResourceCollaborator import ResourceCollaborator
from manager.ResourcesManager import ResourcesManager
from model.Data import Role
from model.Resource import Resource
from staff.TaskManager import TaskManager
from util import Log


class StaffMember(ResourceCollaborator):
    name: str
    role: Role
    task_manager: TaskManager

    def __init__(self, name: str, role: Role, resources_manager: ResourcesManager):
        super().__init__(resources_manager, role.inputs)
        self.name = name
        self.role = role
        self.task_manager = TaskManager(role.tasks, role.outputs)

    def create_output_resources(self, available_resources: list[Resource]) -> list[Resource]:
        print("\n")
        Log.p(
            f"{self.role.name} ({self.name}) has resources ({self.role.inputs}) - working on: {self.role.outputs}")
        self.task_manager.execute_tasks(self.available_resources)

        task_outputs = self.task_manager.output_consumer.get_resources()
        return task_outputs
