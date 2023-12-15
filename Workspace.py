from WorkspaceInfo import WorkspaceInfo
from company.Company import Company
from util import JsonUtil, Log
from util.FileManager import FileManager


class Workspace:
    companies: list[Company]

    def __init__(self):
        self.companies = []

    def create_company(self, name: str) -> Company:
        # TODO("Check if company already exists")
        return Company(name)

    def get_company(self, name: str) -> Company:
        for company in self.companies:
            if company.name == name:
                return company
        raise Exception(f"Company not found: {name}")

    def get_or_create_company(self, name: str) -> Company:
        if self.is_company_existing(name):
            Log.p(f"Getting existing company: {name}")
            return self.get_company(name)
        else:
            Log.p(f"Creating new company: {name}")
            return self.create_company(name)

    def is_company_existing(self, name: str):
        for company in self.companies:
            if company.name == name:
                return True
        return False

    def save_company(self, name: str) -> Company:
        # TODO("Check if company already exists")
        FileManager().save_company(self)

        return Company(name)


def init() -> Workspace:
    workspace_json = FileManager.load_workspace_json()
    workspace_info = JsonUtil.from_json(workspace_json, WorkspaceInfo)

    workspace = Workspace()

    # Load companies based on the Workspace Info
    for company in workspace_info.companies:
        print(f"Loading company: {company}")
        workspace.companies.append(FileManager.load_company(company))

    return workspace
