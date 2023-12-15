from company.Company import Company
from util import JsonUtil
from util.FileManager import FileManager


class List:
    pass


class Workspace:
    companies: []
    company_instances: []

    def __init__(self, companies: List):
        self.companies = companies
        self.company_instances = []

    def create_company(self, name: str) -> Company:
        # TODO("Check if company already exists")
        return Company(name)

    def get_company(self, name: str) -> Company:
        for company in self.company_instances:
            if company.name == name:
                return company
        raise Exception(f"Company not found: {name}")

    def get_or_create_company(self, name: str) -> Company:
        if self.is_company_existing(name):
            return self.get_company(name)
        else:
            return Company(name)

    def is_company_existing(self, name: str):
        for company in self.company_instances:
            if company.name == name:
                return True
        return False

    def save_company(self, name: str) -> Company:
        # TODO("Check if company already exists")
        FileManager().save_company(self)

        return Company(name)


def init() -> Workspace:
    workspace_json = FileManager.load_workspace_json()
    workspace = JsonUtil.from_json(workspace_json, Workspace)

    for company in workspace.companies:
        workspace.company_instances.append(FileManager.load_company(company))

    return workspace
