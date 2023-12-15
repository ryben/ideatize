import Workspace
from prompt.Prompt import Prompt


def main():
    company_create_calculator()


def company_create_calculator():
    prompt = Prompt("Create a calculator app")

    Workspace.init().get_or_create_company("Calcutech").receive_prompt(prompt)


main()
