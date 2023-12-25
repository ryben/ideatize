from core.ResourceCollaborator import ResourceCollaborator
from manager.ResourcesManager import ResourcesManager
from model.Resource import Resource


class SkillOutputSink(ResourceCollaborator):

    def __init__(self, resources_manager: ResourcesManager, applicable_input_types: list[str]):
        super().__init__(resources_manager, applicable_input_types)

    def create_output_resources(self, available_resources: list[Resource]) -> list[Resource]:
        return []

    def get_resources(self):
        return self.available_resources

