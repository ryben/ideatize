import traceback

from Executor import Executor
from Project import Project
from prompt.Prompt import Prompt
from prompt.ResearchPrompt import ResearchPrompt


def main():
    ask_to_create_app()


def ask_to_create_app():
    project = Project("sample")
    try:
        Executor(project).start(Prompt("Write a calculator app"))
    except Exception as e:
        print(e)
        traceback.print_exc()


main()
