import json
import os.path

from company.Company import Company
from company.Project import Project
from company.Role import Role
from company.model.CompanyInfo import CompanyInfo
from util import JsonUtil


def get_working_directory():
    return os.getcwd()


class FileManager:
    workspace_folder = "workspace"
    workspace_path = os.path.join(get_working_directory(), workspace_folder)
    workspace_file = "info.json"
    companies_folder = "companies"
    companies_path = os.path.join(workspace_path, companies_folder)
    company_json_file = "info.json"

    @staticmethod
    def load_workspace_json() -> str:
        # Read from file
        workspace_file_path = os.path.join(FileManager.workspace_path, FileManager.workspace_file)
        f = open(workspace_file_path, "r")
        workspace_json = f.read()
        f.close()

        return workspace_json

    @staticmethod
    def load_company(company_folder) -> Company:
        company_json_file = os.path.join(FileManager.companies_path,
                                         company_folder,
                                         FileManager.company_json_file)
        f = open(company_json_file, "r")
        company_info: CompanyInfo
        company_info = JsonUtil.from_json(f.read(), CompanyInfo)
        f.close()

        company = Company(company_info.name)
        company.roles = FileManager.load_roles(company_info.roles)
        company.projects = FileManager.load_projects(company_info.roles)

        return company

    @staticmethod
    def load_projects(projects: list[str]) -> list[Project]:
        return []

    @staticmethod
    def load_roles(roles: list[str]) -> list[Role]:
        return []

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
