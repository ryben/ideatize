from dataclasses import dataclass
from typing import List


@dataclass
class Role:
    name: str
    inputs: List[str]
    outputs: List[str]
    tasks: List[str]


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
    output: str
    details: str
    script_file: str


@dataclass
class Workspace:
    companies: List[Company]
