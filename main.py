from manager.CompanyManager import CompanyManager
from manager.WorkspaceManager import WorkspaceManager
from model.Prompt import Prompt
from skills.BaseSkill import BaseSkill
from util.ResourceFactory import ResourceFactory
from util.SkillLoader import SkillLoader


def main():
    prompt = Prompt("Create a calculator app")

    company = WorkspaceManager().get_company("Calcutech")
    company_manager = CompanyManager(company)
    company_manager.receive_resource(ResourceFactory.create("Researched Topic", "Kathniel"))

main()
