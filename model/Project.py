from dataclasses import dataclass

from model.Employee import Employee
from model.Session import Session


@dataclass
class Project:
    sessions: list[Session]
    collaborators: list[Employee]
