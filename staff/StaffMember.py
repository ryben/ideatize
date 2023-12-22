from core.BaseSubscriber import BaseSubscriber
from manager.ResourcesManager import ResourcesManager
from model.Data import Role, Output
from model.Resource import Resource
from util import Log


class StaffMember(BaseSubscriber):
    name: str
    role: Role
    resources_manager: ResourcesManager
    available_resources: list[Resource]

    def __init__(self, name: str, role: Role, resources_manager: ResourcesManager):
        self.name = name
        self.role = role
        self.available_resources = []
        self.resources_manager = resources_manager

    def on_get_update(self, resource):
        if resource.type in self.role.inputs:
            self.on_receive_applicable_resource(resource)

    def on_receive_applicable_resource(self, resource: Resource):
        Log.p(f"{self.role.name} ({self.name})"
              f"\n\t receiving:   {resource.type}")
        self.available_resources.append(resource)

        if self.has_all_needed_resources():
            Log.p(f"{self.role.name} ({self.name}) has all needed resources ({self.role.inputs})"
                  f"\n\t working on: {self.role.outputs}\n")
            for output in self.role.outputs:
                self.do_output(output)

    def has_all_needed_resources(self):
        types_of_available_resources = set()
        for available_resource in self.available_resources:
            types_of_available_resources.add(available_resource.type)

        return set(self.role.inputs) == types_of_available_resources

    def do_output(self, output: Output):
        self.resources_manager.add_resource(Resource(output.name, ""))
