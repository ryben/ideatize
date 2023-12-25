from manager.CompanyManager import CompanyManager
from manager.WorkspaceManager import WorkspaceManager
from model.Prompt import Prompt
from skills.BaseSkill import BaseSkill
from util.ResourceFactory import ResourceFactory
from util.SkillLoader import SkillLoader


def main():
    company = WorkspaceManager().get_company("Calcutech")
    company_manager = CompanyManager(company)
    company_manager.receive_resource(ResourceFactory.create("Prompt", "Trending topic right now on social media"))


main()
