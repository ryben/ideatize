from core.BasePublisher import BasePublisher
from model.Prompt import Prompt
from model.Resource import Resource


class ResourcesManager(BasePublisher):
    resources: list[Resource]

    def __init__(self):
        super().__init__()
        self.resources = []

    def create_from_prompt(self, prompt: Prompt) -> Resource:
        resource = Resource("Prompt", "Resource content")
        resource.content = prompt.content
        return resource

    def add_resource(self, resource: Resource):
        # Log.p(f"Adding resource: {resource.type}")
        self.resources.append(resource)
        self.notify_staff_members(resource)

    def notify_staff_members(self, resource: Resource):
        self.notify_observers(resource)
