from manager.ResourcesManager import ResourcesManager
from model.Resource import Resource
from staff.SkillOutputSink import SkillOutputSink
from staff.StaffSkill import StaffSkill
from util import JsonUtil
from util.SkillLoader import SkillLoader


class SkillManager:
    skills: list[StaffSkill]
    resources_manager: ResourcesManager
    skill_loader: SkillLoader
    output_consumer: SkillOutputSink

    def __init__(self, skill_names: list[str], skill_inputs: list[str], skill_outputs: list[str]):
        self.skills = []
        self.resources_manager = ResourcesManager()
        self.skill_loader = SkillLoader()

        self.output_consumer = SkillOutputSink(self.resources_manager, skill_outputs)
        self.resources_manager.subscribe(self.output_consumer)

        # Setup skills so that they take inputs and send outputs to each other
        for skill_name in skill_names:
            base_skill = self.skill_loader.load_by_name(skill_name)
            staff_skill = StaffSkill(base_skill, self.resources_manager)
            self.skills.append(staff_skill)
            self.resources_manager.subscribe(staff_skill)

    def execute_skills(self, resources: list[Resource]):
        for resource in resources:
            self.resources_manager.add_resource(resource)
