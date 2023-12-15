import Workspace
from prompt.Prompt import Prompt


def main():
    company_create_calculator()


def company_create_calculator():
    prompt = Prompt("Create a calculator app")
    workspace = Workspace.init()
    print(f"Saved Companies: {workspace.companies}")

    Workspace.init().get_or_create_company("Calcutech").receive_prompt(prompt)


main()
