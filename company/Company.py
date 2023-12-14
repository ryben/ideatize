from typing import List

from company import Role
from company.Project import Project
from prompt.Prompt import Prompt
from resource.ResourceFactory import ResourceFactory


class Company:
    name: str
    roles: List[Role]
    projects: List[Project]

    def __init__(self, name: str):
        self.name = name
        self.roles = []
        self.projects = []
        pass

    def receive_prompt(self, prompt: Prompt):
        # TODO("Auto name the project based on the prompt")
        project = self.create_project("Calculator")
        self.projects.append(project)
        self.start_project_from_prompt(project, prompt)

    def start_project_from_prompt(self, project: Project, prompt: Prompt):
        session = project.create_session()
        session.resource_manager.add_resource(ResourceFactory.fromPrompt(prompt))
        session.session_manager.work()

    def create_project(self, name: str) -> Project:
        # TODO("Load a company from file")
        team_members = []
        return Project(name, team_members)


def of_name(self, name: str) -> Company:
    # TODO("Load a company from file")
    return Company(name)
