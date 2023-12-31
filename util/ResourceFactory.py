from model.Prompt import Prompt
from model.Resource import Resource
from util import FileManager


class ResourceFactory:
    @staticmethod
    def create_from_prompt(prompt: Prompt) -> Resource:
        resource = Resource("Prompt", "Resource content")
        resource.content = prompt.content
        return resource

    @staticmethod
    def create(resource_type: str, content: str) -> Resource:
        return Resource(resource_type, content)

    @staticmethod
    def create_from_file(resource_type: str, filename: str) -> Resource:
        content = FileManager.read_file_from_workspace(filename)
        return Resource(resource_type, content)
