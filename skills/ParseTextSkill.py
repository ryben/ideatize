from skills.BaseSkill import BaseSkill


class ParseTextSkill(BaseSkill):
    def __init__(self):
        super().__init__()

    def process_inputs(self, inputs):
        print(f"Executing parse skill for {inputs}")
        return "Executed parse skill"

