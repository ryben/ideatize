from dataclasses import dataclass


@dataclass
class Link:
    name: str
    to: str