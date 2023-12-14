from dataclasses import dataclass
from typing import List


@dataclass
class Role:
    name: str
    input_types: List[str]
    output_types: List[str]
    skills: List[str]

