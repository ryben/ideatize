from typing import List

from company.model import Role
from resource.Resource import Resource
from tasking.Task import Task
from tasking.TaskStatus import TaskStatus
from util import Log


class TeamMember:
    name: str
    role: Role
    tasks: List[Task]

    def __init__(self, name: str, role: Role):
        self.name = name
        self.role = role
        self.tasks = []

    def get_input_types(self) -> List[str]:
        return self.role.input_types

    def get_output_types(self) -> List[str]:
        return self.role.output_types

    def get_skills(self) -> List[str]:
        return self.role.skills

    def needs_resource(self, resource: Resource) -> bool:
        for task in self.tasks:
            if task.needs_resource(resource):
                return True
        return False

    def get_task_needing_resource(self, resource: Resource) -> Task:
        for task in self.tasks:
            if task.needs_resource(resource):
                return task
        # If no task that need that resource yet, create a new one
        task = Task(self.role.input_types)
        return task

    def add_task(self, task: Task):
        self.tasks.append(task)

    def work(self) -> list[Resource]:
        outputs: list[Resource] = []
        for task in self.tasks:
            if task.is_ready():
                self.log(f"TaskStatus -> {TaskStatus.IN_PROGRESS}")
                task.status = TaskStatus.IN_PROGRESS
                outputs.extend(self.do_task(task))
                self.log(f"TaskStatus -> {TaskStatus.DONE}")
                task.status = TaskStatus.DONE
        return outputs

    def do_task(self, task: Task) -> list[Resource]:
        outputs: list[Resource] = []
        for output_type in self.role.output_types:
            self.log(f"Doing task {task} -> Output: {output_type.name}")
            # TODO("Do actual task")
            output_resource = Resource(output_type, f"Output by {self.name} ({self.role.role})")
            outputs.append(output_resource)
        return outputs

    def log(self, msg: str):
        Log.p(f"{self.name} ({self.role.role}): {msg}")
