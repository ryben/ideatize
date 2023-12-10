import logging
import os.path
from typing import List

from Project import Project
from agency.Agent import Agent
from tasking.graph.TaskingGraph import TaskingGraph
from util import JsonUtil


def get_working_directory():
    return os.getcwd()


class FileManager:
    workspace_folder = "workspace"
    agents_folder = "agents"
    session_folder = "sessions"
    tasking_graph_file = "tasking_graph.json"

    def __init__(self, project: Project):
        self.project = project

    def load_tasking_graph(self) -> TaskingGraph:
        tasking_graph: TaskingGraph([], [])

        tasking_graph_path = os.path.join(get_working_directory(),
                                          self.workspace_folder,
                                          self.project.name,
                                          self.tasking_graph_file)

        if os.path.isfile(tasking_graph_path):
            f = open(tasking_graph_path)
            tasking_graph = JsonUtil.from_json(f.read())
        else:
            raise Exception(f"Tasking Graph file not found: {tasking_graph_path}")

        return tasking_graph

    def load_agents(self) -> List[Agent]:
        agents_path = os.path.join(get_working_directory(),
                                   self.workspace_folder,
                                   self.project.name,
                                   self.agents_folder)

        agents = []

        if os.path.isdir(agents_path):
            for file in os.listdir(agents_path):
                file_path = os.path.join(agents_path, file)

                if os.path.isfile(file_path):
                    f = open(file_path)
                    try:
                        agents.append(JsonUtil.from_json(f.read()))
                        print(f"Loading agent {file}")
                    except Exception as e:
                        pass

        else:
            logging.warning(f"Creating missing agents folder: {agents_path}")
            os.mkdir(agents_path)

        return agents

    def save_task(self):
        pass
