from dataclasses import dataclass

from prompt.Prompt import Prompt


@dataclass
class ResearchPrompt(Prompt):
    content: str
