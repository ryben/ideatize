from manager.CompanyManager import CompanyManager
from manager.WorkspaceManager import WorkspaceManager
from util.ResourceFactory import ResourceFactory


def main():
    company = WorkspaceManager().get_company("Calcutech")
    company_manager = CompanyManager(company)
    resource = ResourceFactory.create("File Path", "output.txt")
    resource2 = ResourceFactory.create("App Prototype", "Test file content")
    company_manager.receive_resources([resource, resource2])


main()
