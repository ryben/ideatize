from manager.ResourcesManager import ResourcesManager
from model.Data import Session
from model.StaffMember import StaffMember
from resource.Resource import Resource
from util import Log


class SessionManager:
    session: Session
    resources_manager: ResourcesManager
    staff_members: list[StaffMember]

    def __init__(self, session: Session, staff: list[StaffMember]):
        self.session = session
        self.staff_members = staff
        self.resources_manager = ResourcesManager()

        # Make all staff observe/subscribe to the resources manager
        for staff_member in self.staff_members:
            self.resources_manager.attach(staff_member)

    def receive_resource(self, resource: Resource):
        Log.p(f"Receiving resource: {resource.type}")
        self.receive_resources([resource])

    def receive_resources(self, resources: list[Resource]):
        Log.p(f"Processing {len(resources)} resource(s)")
        for resource in resources:
            self.resources_manager.add_resource(resource)
            # self.session_manager.assign_tasks_for_resource(resource)
            #
            # # Let members do their tasks, which returns resources
            # outputs: list[Resource] = self.session_manager.get_outputs_from_members()
            # self.receive_resources(outputs)
