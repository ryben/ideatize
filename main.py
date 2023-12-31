from manager.CompanyManager import CompanyManager
from manager.WorkspaceManager import WorkspaceManager
from util.ResourceFactory import ResourceFactory


def main():
    company = WorkspaceManager().get_company("Calcutech")
    company_manager = CompanyManager(company)
    resource = ResourceFactory.create_from_file("App Feature Set",
                                                "2023-12-30 07.51.33 - Perry Scope - App Feature Set.log")
    company_manager.receive_resource(resource)


main()
