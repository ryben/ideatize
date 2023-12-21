class BaseSkill:
    def __init__(self):
        self.inputs = None
        self.outputs = None

    def set_inputs(self, inputs):
        self.inputs = inputs

    def execute(self):
        pass

    def get_outputs(self):
        return self.outputs
