from model.Prompt import Prompt
from model.Resource import Resource


class ResourceFactory:
    @staticmethod
    def create_from_prompt(prompt: Prompt) -> Resource:
        resource = Resource("Prompt", "Resource content")
        resource.content = prompt.content
        return resource
