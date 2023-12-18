from dataclasses import dataclass

from model.Project import Project
from model.Role import Role


@dataclass
class Company:
    name: str
    roles: list[Role]
    projects: list[Project]
