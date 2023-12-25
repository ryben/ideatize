from core.ResourceCollaborator import ResourceCollaborator
from manager.ResourcesManager import ResourcesManager
from model.Data import Role
from model.Resource import Resource
from staff.SkillManager import SkillManager
from util import Log


class StaffMember(ResourceCollaborator):
    name: str
    role: Role
    skill_manager: SkillManager

    def __init__(self, name: str, role: Role, resources_manager: ResourcesManager):
        super().__init__(resources_manager, role.inputs)
        self.name = name
        self.role = role
        self.skill_manager = SkillManager(role.skills, role.outputs)

    def create_output_resources(self, available_resources: list[Resource]) -> list[Resource]:
        print("\n")
        Log.p(
            f"{self.role.name} ({self.name}) has resources ({self.role.inputs}) - working on: {self.role.outputs}")
        self.skill_manager.execute_skills(self.available_resources)

        skill_outputs = self.skill_manager.output_consumer.get_resources()
        return skill_outputs
