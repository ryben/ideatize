from dataclasses import dataclass


@dataclass
class Task:
    assignee: str
    content: str
