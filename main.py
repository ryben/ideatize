from Prompt import Prompt
from ResearchPrompt import ResearchPrompt
from TaskFactory import TaskFactory
from TaskManager import TaskManager

user_input = input("What do you want to do?\n> ")
prompt = ResearchPrompt(user_input)

task = TaskFactory.from_source(prompt)
TaskManager().add_task(task)
