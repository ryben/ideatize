from skills.BaseSkill import BaseSkill


class LLM(BaseSkill):
    def __init__(self):
        super().__init__()

    def execute(self, inputs):
        print(f"Processing inputs: {inputs}")
        return "Used LLM to generate an output"
