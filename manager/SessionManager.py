from manager.ResourcesManager import ResourcesManager
from model.Data import Session, Staff, Role
from staff.StaffMember import StaffMember
from model.Resource import Resource
from util import Log


class SessionManager:
    session: Session
    resources_manager: ResourcesManager
    staff_members: list[StaffMember]

    def __init__(self, session: Session, staff_list: list[Staff], roles: list[Role]):
        self.session = session
        self.roles = roles
        self.resources_manager = ResourcesManager()
        self.staff_members = []

        for staff in staff_list:
            self.staff_members.append(StaffMember(staff.name, self.find_role_by_name(staff.role), self.resources_manager))

        # Make all staff observe/subscribe to the resources manager
        for staff_member in self.staff_members:
            self.resources_manager.subscribe(staff_member)

    def find_role_by_name(self, role_name) -> Role:
        for role in self.roles:
            if role.name == role_name:
                return role

    def receive_resource(self, resource: Resource):
        Log.p(f"Receiving resource: {resource.type}")
        self.add_resource(resource)

    def receive_resources(self, resources: list[Resource]):
        Log.p(f"Processing {len(resources)} resource(s)")
        for resource in resources:
            self.add_resource(resource)

    def add_resource(self, resource: Resource):
        self.resources_manager.add_resource(resource)
