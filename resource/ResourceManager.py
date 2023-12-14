from typing import List

from resource.Resource import Resource


class ResourceManager:
    resources: List[Resource]

    def __init__(self):
        self.resources = []

    def add_resource(self, resource: Resource):
        self.resources.append(resource)
