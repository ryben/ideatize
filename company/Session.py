from company.SessionManager import SessionManager
from resource.Resource import Resource


class Session:
    session_manager: SessionManager

    def __init__(self, session_manager: SessionManager):
        self.session_manager = session_manager

    def receive_resource(self, resource: Resource):
        self.receive_resources([resource])

    def receive_resources(self, resources: list[Resource]):
        if len(resources) > 0:
            for resource in resources:
                self.session_manager.add_resource(resource)
                self.session_manager.generate_tasks_from_resource(resource)

                # Let members do their tasks, which returns resources
                outputs: list[Resource] = self.session_manager.get_outputs_from_members()
                self.receive_resources(outputs)
