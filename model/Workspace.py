from model import FileManager
from model.Company import Company
from util import JsonUtil


class Workspace:
    companies: list[Company]

    def __init__(self, companies: list[Company]):
        self.companies = companies

    @staticmethod
    def instance():
        workspace_json = FileManager.load_workspace_json("workspace.json")
        obj = JsonUtil.json_to_object(workspace_json)
        return Workspace(obj['companies'])

    def get_company(self, name: str):
        for company in self.companies:
            if company.name == name:
                return company


