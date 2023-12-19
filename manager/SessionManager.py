from manager.ResourcesManager import ResourcesManager
from model.Data import Session
from model.StaffMember import StaffMember
from resource.Resource import Resource
from util import Log


class SessionManager:
    session: Session
    resources_manager: ResourcesManager
    staff_members: list[StaffMember]

    def __init__(self, session: Session, staff_members: list[StaffMember]):
        self.session = session
        self.staff_members = staff_members
        self.resources_manager = ResourcesManager()

        # Make all staff observe/subscribe to the resources manager
        for staff_member in self.staff_members:
            self.resources_manager.attach(staff_member)
            staff_member.set_resources_manager(self.resources_manager)

    def receive_resource(self, resource: Resource):
        Log.p(f"Receiving resource: {resource.type}")
        self.resources_manager.add_resource(resource)

    def receive_resources(self, resources: list[Resource]):
        Log.p(f"Processing {len(resources)} resource(s)")
        for resource in resources:
            self.resources_manager.add_resource(resource)
