from manager.ProjectManager import ProjectManager
from model.Data import Company, Project, Staff
from model.Prompt import Prompt
from util import Log


class CompanyManager:
    company: Company
    project_managers: list[ProjectManager]

    def __init__(self, company: Company):
        self.company = company
        self.project_managers = []
        for project in company.projects:
            self.project_managers.append(ProjectManager(project, company.roles))

    def receive_prompt(self, prompt: Prompt):
        Log.p(f"Prompt received: {prompt}")
        project = self.get_or_create_project("Calculator")
        self.execute_project_from_prompt(project, prompt)

    def execute_project_from_prompt(self, project: Project, prompt: Prompt):
        project_manager = self.get_project_manager(project)
        session = project_manager.create_session()
        session_manager = project_manager.get_session_manager(session)
        session_manager.receive_resource(session_manager.resources_manager.create_from_prompt(prompt))

    def get_project_manager(self, project) -> ProjectManager:
        for project_manager in self.project_managers:
            if project_manager.project == project:
                return project_manager

    def create_project(self, name: str) -> Project:
        Log.p(f"Creating project: {name}")

        staff = self.assemble_staff()
        names = []
        for member in staff:
            names.append(member.name)
        Log.p(f"Project {name} team members: {",".join(names)}")

        project = Project(name, staff, [])
        self.project_managers.append(ProjectManager(project, self.company.roles))
        self.company.projects.append(project)

        return project

    def get_project(self, name: str):
        for project in self.company.projects:
            if project.name == name:
                return project
        raise Exception(f"Project not found: {name}")

    def get_or_create_project(self, name: str) -> Project:
        if self.is_project_existing(name):
            Log.p(f"Getting existing project: {name}")
            return self.get_project(name)
        else:
            Log.p(f"Creating new project: {name}")
            project = self.create_project(name)
            return project

    def is_project_existing(self, name: str):
        for project in self.company.projects:
            if project.name == name:
                return True
        return False

    def assemble_staff(self) -> list[Staff]:
        team_member = Staff("Rey", self.roles[0])
        return [team_member]
