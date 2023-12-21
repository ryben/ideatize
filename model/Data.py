from dataclasses import dataclass
from typing import List


@dataclass
class Output:
    name: str
    instructions: str


@dataclass
class Role:
    name: str
    inputs: List[str]
    outputs: List[Output]
    skills: List[str]


@dataclass
class Staff:
    name: str
    role: str


@dataclass
class Session:
    id: str


@dataclass
class Project:
    name: str
    staff: List[Staff]
    sessions: List[Session]


@dataclass
class Company:
    name: str
    roles: List[Role]
    projects: List[Project]


@dataclass
class Skill:
    name: str
    inputs: List[str]
    outputs: List[str]


@dataclass
class Workspace:
    companies: List[Company]
    skills: List[Skill]
