from core.ResourceCollaborator import ResourceCollaborator
from manager.ResourcesManager import ResourcesManager
from model.Resource import Resource
from skills.BaseTask import BaseTask


class StaffTask(ResourceCollaborator):
    base_task: BaseTask

    def __init__(self, base_task: BaseTask, resources_manager: ResourcesManager):
        super().__init__(resources_manager, base_task.inputs)
        self.base_task = base_task

    def create_output_resources(self, available_resources: list[Resource]) -> list[Resource]:
        base_task_inputs = {}

        # Map resources using input types as keys
        for resource in self.available_resources:
            base_task_inputs[resource.type] = resource.content

        task_output = self.base_task.execute(base_task_inputs)
        output_resource = Resource(self.base_task.output, task_output)
        print(f"Output resource: {output_resource.type} - {output_resource.content}")

        return [output_resource]
