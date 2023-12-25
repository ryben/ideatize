import importlib
import importlib.util

from model.Data import Skill
from skills.BaseSkill import BaseSkill
from util import FileManager, JsonUtil


class SkillLoader:
    skills_package: str
    skills: list[Skill]

    def __init__(self, skills_json: str = "skills.json", skills_package: str = "skills"):
        self.skills_package = skills_package
        self.skills = JsonUtil.from_json(FileManager.load_data_json(skills_json), list[Skill])

    def load_by_name(self, skill_name: str) -> BaseSkill:
        for skill in self.skills:
            if skill.name == skill_name:
                base_skill = self.load(skill.script_file)
                base_skill.inputs = skill.inputs
                base_skill.outputs = skill.outputs
                return base_skill

    def load(self, skill_file_name) -> BaseSkill:
        module_name = skill_file_name.replace('.py', '')
        skill_module = importlib.import_module(".".join([self.skills_package, module_name]))

        for cls_name, cls in skill_module.__dict__.items():
            if isinstance(cls, type) and issubclass(cls, BaseSkill) and cls is not BaseSkill:
                return cls()

        raise ValueError(f"No subclass of {BaseSkill.__name__} found in {skill_file_name}")
