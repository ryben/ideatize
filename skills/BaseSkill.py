from abc import abstractmethod


class BaseSkill:
    def __init__(self, inputs=None, outputs=None):
        if outputs is None:
            outputs = []
        if inputs is None:
            inputs = []
        self.inputs = inputs
        self.outputs = outputs

    @abstractmethod
    def process_inputs(self, inputs):
        pass

    def execute(self):
        return self.process_inputs(self.inputs)

    def get_outputs(self):
        return self.outputs
