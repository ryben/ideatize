import json
from types import SimpleNamespace

from Project import Project
from tasking.graph.TaskingGraph import TaskingGraph
import os.path


def get_working_directory():
    return os.getcwd()


class FileManager:
    workspace_folder_name = "workspace"
    session_folder_name = "sessions"
    tasking_graph_filename = "tasking_graph.json"

    def load_tasking_graph(self, project: Project) -> TaskingGraph:
        tasking_graph: TaskingGraph()

        tasking_graph_path = os.path.join(get_working_directory(),
                                          self.workspace_folder_name,
                                          project.name,
                                          self.tasking_graph_filename)

        if os.path.isfile(tasking_graph_path):
            f = open(tasking_graph_path)
            tasking_graph = json.loads(f.read(), object_hook=lambda d: SimpleNamespace(**d))
        else:
            raise Exception(f"Tasking Graph file not found: {tasking_graph_path}")

        return tasking_graph

    def load_agents(self):
        pass

    def save_task(self):
        pass
