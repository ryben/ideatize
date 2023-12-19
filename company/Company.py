from typing import List

from company.Project import Project
from company.model.Role import Role
from company.TeamMember import TeamMember
from prompt.Prompt import Prompt
from resource.ResourceFactory import ResourceFactory
from util import Log


class Company:
    name: str
    roles: List[Role]
    projects: List[Project]

    def __init__(self, name: str, roles: list[Role], projects: list[Project]):
        self.name = name
        self.roles = roles
        self.projects = projects

    def receive_prompt(self, prompt: Prompt):
        Log.p(f"Prompt received: {prompt}")
        project = self.get_or_create_project("Calculator")
        self.projects.append(project)
        self.execute_project_from_prompt(project, prompt)

    def execute_project_from_prompt(self, project: Project, prompt: Prompt):
        session = project.create_session()
        resource = ResourceFactory.fromPrompt(prompt)
        session.receive_resource(resource)

    def create_project(self, name: str) -> Project:
        Log.p(f"Creating project: {name}")

        team_members = self.assemble_team()
        names = []
        for member in team_members:
            names.append(member.name)
        Log.p(f"Project {name} team members: {",".join(names)}")

        return Project(name, team_members)

    def get_project(self, name: str):
        for project in self.projects:
            if project.name == name:
                return project
        raise Exception(f"Project not found: {name}")

    def get_or_create_project(self, name: str) -> Project:
        if self.is_project_existing(name):
            Log.p(f"Getting existing project: {name}")
            return self.get_project(name)
        else:
            Log.p(f"Creating new project: {name}")
            return self.create_project(name)

    def is_project_existing(self, name: str):
        for project in self.projects:
            if project.name == name:
                return True
        return False

    def assemble_team(self) -> list[TeamMember]:
        team_member = TeamMember("Rey", self.roles[0])
        return [team_member]

    @staticmethod
    def of_name(name: str):
        """Load company from file"""
        new_company = Company(name)
