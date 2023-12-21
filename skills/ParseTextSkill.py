from skills.BaseSkill import BaseSkill


class ParseTextSkill(BaseSkill):
    def execute(self):
        self.outputs = self.inputs.split()

