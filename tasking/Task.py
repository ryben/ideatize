from typing import List

from resource.Resource import Resource
from tasking.TaskStatus import TaskStatus


class Task:
    __resources: List[Resource]
    needed_resource_types: List[str]
    status: TaskStatus

    def __init__(self, needed_resources: List[str]):
        self.__resources = []
        self.needed_resource_types = needed_resources
        self.status = TaskStatus.MISSING_RESOURCE  # All tasks have required resources before they can be worked on

    def add_resource(self, resource: Resource):
        self.__resources.append(resource)
        self.needed_resource_types.remove(resource.type)
        if len(self.needed_resource_types) == 0:
            self.status = TaskStatus.READY

    def needs_resource(self, resource: Resource) -> bool:
        return resource.type in self.needed_resource_types

    def is_ready(self) -> bool:
        return self.status == TaskStatus.READY
