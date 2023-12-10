from agency.AgentManager import AgentManager
from prompt.ResearchPrompt import ResearchPrompt
from tasking.TaskFactory import TaskFactory
from tasking.TaskManager import TaskManager

user_input = input("What app do you want to create?\n> ")
prompt = ResearchPrompt(user_input)

task = TaskFactory.from_source(prompt)

task_manager = TaskManager()
task_manager.push_task(task)

agent_manager = AgentManager(task_manager)
agent_manager.start()
