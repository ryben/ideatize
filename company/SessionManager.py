from typing import List

from company.TeamMember import TeamMember
from resource.Resource import Resource
from resource.ResourceManager import ResourceManager
from tasking.TaskManager import TaskManager
from util import Log


class SessionManager:
    def __init__(self, resource_manager: ResourceManager, task_manager: TaskManager, team_members: List[TeamMember]):
        self.task_manager = task_manager
        self.team_members = team_members
        self.resource_manager = resource_manager

    def add_resource(self, resource: Resource):
        self.resource_manager.add_resource(resource)

    def generate_tasks_from_resource(self, resource: Resource):
        Log.p(f"Looking for members that need the resource: {resource.type}")
        for member in self.team_members:
            # Check among team members who needs the Resource
            if resource.type in member.get_input_types():
                Log.p(f"{member.name} ({member.role.role}) needs the resource: {resource.type}")

                task = member.get_task_needing_resource(resource)
                task.attack_resource(resource)
                self.task_manager.add_task(task)

                Log.p(f"Assigning task to {member.name} ({member.role.role})")
                member.add_task(task)

    def get_outputs_from_members(self) -> list[Resource]:
        outputs: list[Resource] = []
        for member in self.team_members:
            outputs.extend(member.work())
        return outputs
