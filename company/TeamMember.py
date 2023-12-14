from typing import List

from company import Role
from resource.Resource import Resource
from tasking.Task import Task


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

    def work(self):
        print(f"{self.name} working on task: {self.tasks}")
        # TODO("Work on tasks")
        pass
