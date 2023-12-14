from company.Company import Company
from prompt.Prompt import Prompt


def main():
    company_create_calculator()


def company_create_calculator():
    Company("Calcutech").receive_prompt(Prompt("Create a calculator app"))


main()
