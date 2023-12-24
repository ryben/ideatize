from manager.ResourcesManager import ResourcesManager
from model.Data import Skill
from model.Resource import Resource
from skills.BaseSkill import BaseSkill
from util.SkillLoader import SkillLoader


class SkillManager:
    skills: list[BaseSkill]
    resources_manager: ResourcesManager
    skill_loader: SkillLoader

    def __init__(self, skill_names: list[str]):
        self.skills = []
        self.resources_manager = ResourcesManager()
        self.skill_loader = SkillLoader()

        for skill_name in skill_names:
            self.skills.append(self.skill_loader.load_by_name(skill_name))

    def create_output_resources(self) -> list[Resource]:
        pass

