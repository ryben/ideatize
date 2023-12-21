from manager.CompanyManager import CompanyManager
from manager.WorkspaceManager import WorkspaceManager
from model.Prompt import Prompt
from skills.BaseSkill import BaseSkill
from skills.ParseTextSkill import ParseTextSkill


def main():
    prompt = Prompt("Create a calculator app")

    company = WorkspaceManager().get_company("Calcutech")
    company_manager = CompanyManager(company)
    company_manager.receive_prompt(prompt)

    skill: BaseSkill = ParseTextSkill()
    skill.set_inputs("This is a test skill")
    skill.execute()
    print(skill.get_outputs())


main()
