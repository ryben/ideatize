from resource.Resource import Resource
from util import Log


class ResourcesManager:
    resources: list[Resource]

    def __init__(self):
        self.resources = []

    def add_resource(self, resource: Resource):
        Log.p(f"Adding resource: {resource.type}")
        self.resources.append(resource)