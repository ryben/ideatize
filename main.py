import traceback

from Executor import Executor
from Project import Project
from prompt.ResearchPrompt import ResearchPrompt


def main():
    project = Project("sample")
    try:
        executor = Executor(project)
        user_input = input("What app do you want to create?\n> ")
        executor.start(ResearchPrompt(user_input))
    except Exception as e:
        print(e)
        traceback.print_exc()


main()



