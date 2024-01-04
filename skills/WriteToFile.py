from skills.BaseTask import BaseTask


class WriteToFile(BaseTask):
    def __init__(self):
        super().__init__()

    def execute(self, inputs):
        filepath = inputs[0]
        content = inputs[1]

        f = open(filepath, "w")
        f.write(content)
        f.close()

        return filepath
