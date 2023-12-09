from dataclasses import dataclass

from Prompt import Prompt


@dataclass
class ResearchPrompt(Prompt):
    content: str
