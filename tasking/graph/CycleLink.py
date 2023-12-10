from dataclasses import dataclass
from typing import List

from tasking.graph.Link import Link


@dataclass
class CycleLink:
    name: str
    to: List[Link]
