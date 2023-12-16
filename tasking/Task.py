from typing import List

from resource.Resource import Resource
from tasking.TaskStatus import TaskStatus
from util import Log


class Task:
    resources: List[Resource]
    needed_resource_types: List[str]
    status: TaskStatus

    def __init__(self, needed_resources: List[str]):
        self.resources = []
        self.needed_resource_types = needed_resources
        self.status = TaskStatus.MISSING_RESOURCE  # All tasks have required resources before they can be worked on

    def attach_resource(self, resource: Resource):
        self.resources.append(resource)
        Log.p(f"Task's needed resource types: {self.needed_resource_types}")
        self.needed_resource_types.remove(resource.type)
        Log.p(f"Updated: {self.needed_resource_types}")
        if len(self.needed_resource_types) == 0:
            self.status = TaskStatus.READY
            Log.p("Task is now READY")

    def needs_resource(self, resource: Resource) -> bool:
        return resource.type in self.needed_resource_types

    def is_ready(self) -> bool:
        return self.status == TaskStatus.READY

    def is_incomplete(self) -> bool:
        return self.status != TaskStatus.MISSING_RESOURCE
