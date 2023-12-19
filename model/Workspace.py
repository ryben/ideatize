from company.Company import Company
from model import FileManager, Data
from util import JsonUtil


class Workspace:
    companies: list[Company]

    def __init__(self, companies: list[Company]):
        self.companies = companies

    @staticmethod
    def instance() -> Workspace:
        workspace_json = FileManager.load_data_json("workspace.json")
        workspace = Data.parse_json_to_dataclass(JsonUtil.json_load(workspace_json))

        return workspace

    def get_company(self, name: str) -> Company:
        for company in self.companies:
            if company.name == name:
                return company
