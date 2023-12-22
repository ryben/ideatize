from core.BasePublisher import BasePublisher
from model.Prompt import Prompt
from model.Resource import Resource


class ResourcesManager(BasePublisher):
    resources: list[Resource]

    def __init__(self):
        super().__init__()
        self.resources = []

    def add_resource(self, resource: Resource):
        self.resources.append(resource)
        self.publish_to_observers(resource)
