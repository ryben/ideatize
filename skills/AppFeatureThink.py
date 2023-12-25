from skills.BaseSkill import BaseSkill


class InternetSearch(BaseSkill):
    def __init__(self):
        super().__init__()

    def execute(self, inputs):
        return "Here are the features for my app idea"
