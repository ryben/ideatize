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
        output_content = self.base_skill.execute()

        for resource in self.available_resources:
            print(f"Available resource: {resource.type} - {resource.content}")
            # TODO("Outputs should be created upon execution of the base skill, using the input resources

        outputs = []
        for output in self.base_skill.outputs:
            print(f"Creating skill output resource: {output} with content {output_content}")
            outputs.append(Resource(output, output_content))
        return outputs


