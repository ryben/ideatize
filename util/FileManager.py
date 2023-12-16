import json
import os.path

from company.Company import Company
from company.Project import Project
from company.TeamMember import TeamMember
from company.model.CompanyInfo import CompanyInfo
from company.model.OutputType import OutputType
from company.model.Role import Role
from util import JsonUtil, Log


def get_working_directory():
    return os.getcwd()


class FileManager:
    workspace_folder = "workspace"
    workspace_path = os.path.join(get_working_directory(), workspace_folder)
    workspace_file = "info.json"
    companies_folder = "companies"
    companies_path = os.path.join(workspace_path, companies_folder)
    company_json_file = "info.json"
    roles_folder = "roles"
    projects_folder = "projects"
    project_file = "info.json"

    @staticmethod
    def load_workspace_json() -> str:
        # Read from file
        workspace_file_path = os.path.join(FileManager.workspace_path, FileManager.workspace_file)
        return FileManager.read_file(workspace_file_path)

    @staticmethod
    def read_file(filepath: str) -> str:
        f = open(filepath, "r")
        content = f.read()
        f.close()
        return content

    @staticmethod
    def load_company(company_folder) -> Company:
        company_folder_path = os.path.join(FileManager.companies_path,
                                           company_folder)
        company_json_file = os.path.join(company_folder_path,
                                         FileManager.company_json_file)
        f = open(company_json_file, "r")
        company_info: CompanyInfo
        company_info = JsonUtil.from_json(f.read(), CompanyInfo)
        f.close()

        company = Company(company_info.name)
        company.roles = FileManager.load_roles(company_folder, company_info.roles)

        projects_folder = os.path.join(company_folder_path, FileManager.projects_folder)
        company.projects = FileManager.load_projects(projects_folder, company_info.projects, company.roles)

        return company

    @staticmethod
    def load_roles(company_folder: str, roles: list[str]) -> list[Role]:
        loaded_roles: list[Role] = []

        roles_folder_path = os.path.join(FileManager.companies_path,
                                         company_folder,
                                         FileManager.roles_folder)
        for role_file in roles:
            print(f"Loading role: {role_file}")
            role_file_path = os.path.join(roles_folder_path, role_file)
            role_json = FileManager.read_file(role_file_path)

            # Parse Json TODO("Use library to parse nested json into object")
            role_obj = JsonUtil.json_load(role_json)
            role = Role(role_obj["role"])
            role.input_types = role_obj["input_types"]
            output_types: list[OutputType] = []
            for output_type in role_obj["output_types"]:
                new_output_type = OutputType(output_type["name"], output_type["instructions"])
                output_types.append(new_output_type)
            role.output_types = output_types
            role.skills = role_obj["skills"]

            loaded_roles.append(role)

        return loaded_roles

    @staticmethod
    def load_projects(projects_folder: str, projects: list[str], roles: list[Role]) -> list[Project]:
        print(f"Loading projects: {projects}")

        loaded_projects: list[Project] = []

        for project in projects:
            project_folder_path = os.path.join(projects_folder,
                                               project)

            project_file_path = os.path.join(project_folder_path, FileManager.project_file)
            project_json = FileManager.read_file(project_file_path)
            project_obj = JsonUtil.json_load(project_json)

            # Load team members by parsing the Json TODO("Use library to parse nested json into object")
            team_members: list[TeamMember] = []
            for member in project_obj["team_members"]:
                name = member["name"]
                role = FileManager.find_role_by_name(member["role"], roles)
                new_member = TeamMember(name, role)
                team_members.append(new_member)

            loaded_project = Project(project_obj["name"], team_members)
            loaded_project.description = project_obj["description"]

            loaded_projects.append(loaded_project)
        return loaded_projects

    @staticmethod
    def find_role_by_name(name: str, roles: list[Role]):
        for role in roles:
            if role.role == name:
                return role

        raise Exception(f"Role not found: {name}")

    @staticmethod
    def save_company(company: Company):
        # Construct the company folder and file path
        company_folder = os.path.join(FileManager.workspace_path,
                                      FileManager.companies_folder,
                                      FileManager.generate_company_folder_name(company))
        company_file = os.path.join(company_folder,
                                    FileManager.company_json_file)

        # Create the company folder
        if not os.path.exists(company_folder):
            os.mkdir(company_folder)

        # Build the JSON for the company
        company_json = {
            "name": company.name,
            "projects": [],
            "roles": []
        }

        # Write to file
        f = open(company_file, "w")
        f.write(json.dumps(company_json, indent=4))
        f.close()

    @staticmethod
    def generate_company_folder_name(company):
        return company.name.replace(" ", "")
