from model.Prompt import Prompt
from model.Resource import Resource


class ResourceFactory:
    @staticmethod
    def create_from_prompt(prompt: Prompt) -> Resource:
        resource = Resource("Prompt", "Resource content")
        resource.content = prompt.content
        return resource

    @staticmethod
    def create(resource_type: str, content: str) -> Resource:
        return Resource(resource_type, content)
