from dataclasses import dataclass

from company.model.OutputType import OutputType


@dataclass
class Role:
    role: str
    input_types: list[str]
    output_types: list[OutputType]
    skills: list[str]

    def __init__(self, role: str):
        self.role = role



