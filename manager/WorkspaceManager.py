from model.Data import Workspace, Company
from util import JsonUtil, FileManager


class WorkspaceManager:
    companies: list[Company]

    def __init__(self):
        workspace_json = FileManager.load_data_json("workspace.json")
        workspace = JsonUtil.from_json(workspace_json, Workspace)
        self.companies = workspace.companies

    def get_company(self, name: str) -> Company:
        for company in self.companies:
            if company.name == name:
                return company
        raise Exception(f"Company not found: {name}")
