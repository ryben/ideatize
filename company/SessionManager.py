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

    def assign_tasks_for_resource(self, resource: Resource):
        Log.p(f"Looking for members that need the resource: {resource.type}")
        is_resource_needed = False
        for member in self.team_members:
            # Check among team members who needs the Resource
            if resource.type in member.get_input_types():
                Log.p(f"{member.name} ({member.role.role}) needs the resource: {resource.type}")
                is_resource_needed = True
                task = member.get_task_needing_resource(resource)

                if task is None:
                    Log.p(f"Creating new task")
                    task = member.create_task()
                    member.add_task(task)
                    self.task_manager.add_task(task)
                Log.p(f"Updating task (with {resource.type}) of {member.name} ({member.role.role})")
                task.attach_resource(resource)
        if not is_resource_needed:
            Log.p(f"No member needs the resource: {resource.type} ------- ")

    def get_outputs_from_members(self) -> list[Resource]:
        outputs: list[Resource] = []
        for member in self.team_members:
            Log.p(f"{member.role.role} ({member.name}) has {len(member.tasks)} task(s).")

            if member.has_ready_task():
                member_outputs = member.work()
                Log.p(f"{member.role.role} ({member.name}) finished work: {len(member_outputs)} outputs")
                outputs.extend(member_outputs)
            elif member.has_task_with_incomplete_resources():
                Log.p(f"{member.role.role} ({member.name}) has tasks with incomplete resources.")
            # else:
            #     Log.p(f"{member.role.role} ({member.name}) has nothing to do.")
        return outputs
