import importlib
import importlib.util

from skills.BaseSkill import BaseSkill

skills_package = "skills"


def load(skill_file_name) -> BaseSkill:
    module_name = skill_file_name.replace('.py', '')
    skill_module = importlib.import_module(".".join([skills_package, module_name]))

    for cls_name, cls in skill_module.__dict__.items():
        if isinstance(cls, type) and issubclass(cls, BaseSkill) and cls is not BaseSkill:
            return cls()

    raise ValueError(f"No subclass of {BaseSkill.__name__} found in {skill_file_name}")
