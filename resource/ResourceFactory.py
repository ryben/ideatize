from prompt.Prompt import Prompt
from resource.Resource import Resource


class ResourceFactory:
    @staticmethod
    def fromPrompt(prompt: Prompt) -> Resource:
        resource = Resource()
        resource.content = prompt.content
        return resource
