from manager.CompanyManager import CompanyManager
from manager.WorkspaceManager import WorkspaceManager
from model.Prompt import Prompt


def main():
    prompt = Prompt("Create a calculator app")

    company = WorkspaceManager().get_company("Calcutech")
    company_manager = CompanyManager(company)
    company_manager.receive_prompt(prompt)


main()
