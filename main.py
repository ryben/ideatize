import traceback

import Workspace
from prompt.Prompt import Prompt


def main():
    prompt = Prompt("Create a calculator app")
    Workspace.init().get_or_create_company("Ryben Productions").receive_prompt(prompt)


main()
