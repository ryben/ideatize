from typing import List

from resource.Resource import Resource
from util import Log


class ResourceManager:
    resources: List[Resource]

    def __init__(self):
        self.resources = []

    def add_resource(self, resource: Resource):
        Log.p(f"Adding resource: {resource.type}")
        self.resources.append(resource)

