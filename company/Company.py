from typing import List

from company.Project import Project
from company.Role import Role
from company.TeamMember import TeamMember
from prompt.Prompt import Prompt
from resource.ResourceFactory import ResourceFactory
from util import Log


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
        Log.p(f"Prompt received: {prompt}")
        project = self.create_project("Calculator")
        self.projects.append(project)
        self.start_project_from_prompt(project, prompt)

    def start_project_from_prompt(self, project: Project, prompt: Prompt):
        session = project.create_session()
        session.resource_manager.add_resource(ResourceFactory.fromPrompt(prompt))

    def create_project(self, project_name: str) -> Project:
        Log.p(f"Creating project: {project_name}")

        # TODO("Load a company from file")

        team_members = self.assemble_team()
        Log.p(f"Project {project_name} team members: {team_members}")

        return Project(project_name, team_members)

    def assemble_team(self) -> List[TeamMember]:
        # TODO("Replace dummy team member")
        role = Role("Developer", ["Prompt"], ["Code"], [])
        team_member = TeamMember("Rey", role)
        return [team_member]

