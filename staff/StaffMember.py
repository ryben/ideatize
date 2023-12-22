from core.BaseSubscriber import BaseSubscriber
from core.ResourceCollaborator import ResourceCollaborator
from manager.ResourcesManager import ResourcesManager
from model.Data import Role, Output
from model.Resource import Resource
from util import Log


class StaffMember(ResourceCollaborator):
    name: str
    role: Role

    def __init__(self, name: str, role: Role, resources_manager: ResourcesManager):
        super().__init__(resources_manager, role.inputs)
        self.name = name
        self.role = role

    def on_receive_applicable_resource(self, resource: Resource):
        Log.p(f"{self.role.name} ({self.name})"
              f"\n\t receiving:   {resource.type}")
        super().on_receive_applicable_resource(resource)

    def create_output_resources(self) -> list[Resource]:
        Log.p(f"{self.role.name} ({self.name}) has all needed resources ({self.role.inputs})"
              f"\n\t working on: {self.role.outputs}\n")
        outputs = []
        for output in self.role.outputs:
            outputs.append(Resource(output.name, ""))
        return outputs
