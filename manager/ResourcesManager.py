from core.BasePublisher import BasePublisher
from resource.Resource import Resource
from util import Log


class ResourcesManager(BasePublisher):
    resources: list[Resource]

    def __init__(self):
        super().__init__()
        self.resources = []

    def add_resource(self, resource: Resource):
        Log.p(f"Adding resource: {resource.type}")
        self.resources.append(resource)
        self.notify_observers(resource)
