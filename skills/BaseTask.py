from abc import abstractmethod


class BaseTask:
    def __init__(self, inputs=None, output=None, details=""):
        if inputs is None:
            inputs = {}
        self.inputs = inputs
        self.output = output
        self.details = details

    @abstractmethod
    def execute(self, input_obj: dict):
        pass
