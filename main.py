from AgentManager import AgentManager
from Prompt import Prompt
from ResearchPrompt import ResearchPrompt
from TaskFactory import TaskFactory
from TaskManager import TaskManager

user_input = input("What do you want to do?\n> ")
prompt = ResearchPrompt(user_input)

task = TaskFactory.from_source(prompt)

task_manager = TaskManager()
task_manager.push_task(task)

agent_manager = AgentManager(task_manager)
agent_manager.start()
