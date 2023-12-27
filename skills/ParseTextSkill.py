from skills.BaseTask import BaseTask


class ParseTextTask(BaseTask):
    def __init__(self):
        super().__init__()

    def execute(self, inputs):
        output = inputs[list(inputs.keys())[0]].split()
        return output
