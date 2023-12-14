from dataclasses import dataclass
from typing import List

from company.Session import Session


@dataclass
class Project:
    name: str
    sessions: List[Session]

    def __init__(self, name: str):
        self.name = name
        pass

    def create_session(self) -> Session:
        return Session()




