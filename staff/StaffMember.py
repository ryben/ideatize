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

    def __init__(self, name: str, role: Role):
        self.name = name
        self.role = role
        self.available_resources = []

    def set_resources_manager(self, resources_manager: ResourcesManager):
        self.resources_manager = resources_manager

    def on_get_update(self, resource):
        self.on_update_from_resources_manager(resource)

    def on_update_from_resources_manager(self, resource: Resource):
        if resource.type in self.role.inputs:
            Log.p(f"{self.role.name} ({self.name})"
                  f"\n\t receiving:   {resource.type}")
            self.available_resources.append(resource)

            if self.has_all_needed_resources():
                Log.p(f"{self.role.name} ({self.name}) has all needed resources ({self.role.inputs})"
                      f"\n\t working on: {self.role.outputs}\n")
                for output in self.role.outputs:
                    self.do_output(resource, output)

    def has_all_needed_resources(self):
        types_of_available_resources = set()
        for available_resource in self.available_resources:
            types_of_available_resources.add(available_resource.type)

        return set(self.role.inputs) == types_of_available_resources

    def do_output(self, resource: Resource, output: Output):
        self.resources_manager.add_resource(Resource(output.name, ""))
