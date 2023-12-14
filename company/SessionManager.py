from typing import List

from company.TeamMember import TeamMember
from resource.Resource import Resource
from tasking.TaskManager import TaskManager


class SessionManager:
    def __init__(self, task_manager: TaskManager, team_members: List[TeamMember]):
        self.task_manager = task_manager
        self.team_members = team_members

    def process_resource(self, resource: Resource):
        for member in self.team_members:
            # Check among team members who needs the Resource
            if resource.type in member.get_input_types():
                task = member.get_task_needing_resource(resource)
                task.add_resource(resource)
                self.task_manager.add_task(task)

                print(f"Assigning task to {member.name}")
                member.add_task(task)
        self.make_team_members_work()

    def make_team_members_work(self):
        for member in self.team_members:
            member.work()
