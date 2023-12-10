from dataclasses import dataclass, field
from typing import List

from sqlalchemy.ext.mutable import MutableList

from tasking.graph.CycleLink import CycleLink
from tasking.graph.Link import Link


@dataclass
class TaskingGraph:
    links: List[Link]
    cycles: List[CycleLink]
