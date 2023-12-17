from dataclasses import dataclass

from model.Project import Project
from model.Role import Role


@dataclass
class Company:
    roles: list[Role]
    projects: list[Project]
