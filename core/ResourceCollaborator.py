from abc import abstractmethod

from core.BaseSubscriber import BaseSubscriber
from manager.ResourcesManager import ResourcesManager
from model.Resource import Resource


class ResourceCollaborator(BaseSubscriber):
    resources_manager: ResourcesManager
    available_resources: list[Resource]
    applicable_input_types: list[str]

    def __init__(self, resources_manager: ResourcesManager, applicable_input_types: list[str]):
        self.available_resources = []
        self.resources_manager = resources_manager
        self.applicable_input_types = applicable_input_types

    def is_applicable_resource(self, resource) -> bool:
        return resource.type in self.applicable_input_types

    def on_get_update(self, resource):
        if self.is_applicable_resource(resource):
            self.on_receive_applicable_resource(resource)

    def on_receive_applicable_resource(self, resource: Resource):
        self.available_resources.append(resource)

        if self.can_start_outputs():
            for output_resource in self.create_output_resources(self.available_resources):
                self.resources_manager.add_resource(output_resource)

    def can_start_outputs(self) -> bool:
        types_of_available_resources = set()
        for available_resource in self.available_resources:
            types_of_available_resources.add(available_resource.type)

        return set(self.applicable_input_types) == types_of_available_resources

    @abstractmethod
    def create_output_resources(self, available_resources: list[Resource]) -> list[Resource]:
        pass
