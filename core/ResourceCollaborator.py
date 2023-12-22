from abc import abstractmethod

from core.BaseSubscriber import BaseSubscriber
from manager.ResourcesManager import ResourcesManager
from model.Resource import Resource


class ResourceCollaborator(BaseSubscriber):
    resources_manager: ResourcesManager
    available_resources: list[Resource]

    def __init__(self):
        self.available_resources = []
        self.resources_manager: ResourcesManager

    @abstractmethod
    def is_applicable_resource(self, resource) -> bool:
        pass

    def on_get_update(self, resource):
        if self.is_applicable_resource(resource):
            self.on_receive_applicable_resource(resource)

    def on_receive_applicable_resource(self, resource: Resource):
        self.available_resources.append(resource)

        if self.can_start_output():
            for output in self.create_outputs():
                self.resources_manager.add_resource(output)

    @abstractmethod
    def can_start_output(self) -> bool:
        pass

    @abstractmethod
    def create_outputs(self) -> list:
        pass
