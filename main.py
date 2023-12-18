from model.Workspace import Workspace
from prompt.Prompt import Prompt


def main():
    prompt = Prompt("Create a calculator app")
    company = Workspace.instance().get_company("Calcutech")
    print(company.name)


main()
