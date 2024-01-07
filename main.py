from manager.CompanyManager import CompanyManager
from manager.WorkspaceManager import WorkspaceManager
from util.ResourceFactory import ResourceFactory


def main():
    company = WorkspaceManager().get_company("Calcutech")
    company_manager = CompanyManager(company)
    resource = ResourceFactory.create("Start Signal", "Go")
    company_manager.receive_resources([resource])


main()
