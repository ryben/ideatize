from manager.CompanyManager import CompanyManager
from manager.WorkspaceManager import WorkspaceManager
from util.ResourceFactory import ResourceFactory


def main():
    company = WorkspaceManager().get_company("Calcutech")
    company_manager = CompanyManager(company)
    company_manager.receive_resource(ResourceFactory.create("Researched Topic", "To do list"))


main()
