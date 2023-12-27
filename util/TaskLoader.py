import importlib
import importlib.util

from model.Data import Skill
from skills.BaseTask import BaseTask
from util import FileManager, JsonUtil


class TaskLoader:
    skills_package: str
    skills: list[Skill]

    def __init__(self, skills_json: str = "tasks.json", skills_package: str = "skills"):
        self.skills_package = skills_package
        self.skills = JsonUtil.from_json(FileManager.load_data_json(skills_json), list[Skill])

    def load_by_name(self, skill_name: str) -> BaseTask:
        for skill in self.skills:
            if skill.name == skill_name:
                base_skill = self.load(skill.script_file)
                base_skill.inputs = skill.inputs
                base_skill.output = skill.output
                base_skill.details = skill.details
                return base_skill

    def load(self, skill_file_name) -> BaseTask:
        module_name = skill_file_name.replace('.py', '')
        skill_module = importlib.import_module(".".join([self.skills_package, module_name]))

        for cls_name, cls in skill_module.__dict__.items():
            if isinstance(cls, type) and issubclass(cls, BaseTask) and cls is not BaseTask:
                return cls()

        raise ValueError(f"No subclass of {BaseTask.__name__} found in {skill_file_name}")
