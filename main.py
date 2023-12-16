import traceback

import Workspace
from prompt.Prompt import Prompt


def main():
    # try:
        company_create_calculator()
    # except Exception as e:
    #     print(f"Error: {e}")
    #     traceback.print_exc()


def company_create_calculator():
    prompt = Prompt("Create a calculator app")

    Workspace.init().get_or_create_company("Ryben Productions").receive_prompt(prompt)


main()
