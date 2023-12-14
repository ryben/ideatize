from typing import List

from Project import Project
from company import Role


class Company:
    name: str
    roles: List[Role]
    projects: List[Project]

    def __init__(self, name: str):
        self.name = name
        pass


def of_name(self, name: str) -> Company:
    # TODO("Load a company from file")
    return Company(name)
