from skills.BaseSkill import BaseSkill


class InternetSearch(BaseSkill):
    def __init__(self):
        super().__init__()

    def execute(self, inputs):
        print(f"Processing inputs: {inputs}")
        return "Here is a sample research about the topic"
