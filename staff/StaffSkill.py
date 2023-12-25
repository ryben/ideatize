from core.ResourceCollaborator import ResourceCollaborator
from manager.ResourcesManager import ResourcesManager
from model.Resource import Resource
from skills.BaseSkill import BaseSkill


class StaffSkill(ResourceCollaborator):
    base_skill: BaseSkill

    def __init__(self, base_skill: BaseSkill, resources_manager: ResourcesManager):
        super().__init__(resources_manager, base_skill.inputs)
        self.base_skill = base_skill

    def create_output_resources(self, available_resources: list[Resource]) -> list[Resource]:
        base_skill_inputs = {}

        # Map resources using input types as keys
        for resource in self.available_resources:
            base_skill_inputs[resource.type] = resource.content

        skill_output = self.base_skill.execute(base_skill_inputs)
        output_resource = Resource(self.base_skill.output, skill_output)
        print(f"Output resource: {output_resource.type} - {output_resource.content}")

        return [output_resource]
