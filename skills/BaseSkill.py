from abc import abstractmethod


class BaseSkill:
    def __init__(self, inputs=None, output=None):
        if inputs is None:
            inputs = {}
        self.inputs = inputs
        self.output = output

    @abstractmethod
    def execute(self, input_obj: dict):
        pass
