from typing import List

from company.SessionManager import SessionManager
from resource.Resource import Resource
from util import Log


class ResourceManager:
    resources: List[Resource]
    session_manager: SessionManager

    def __init__(self, session_manager: SessionManager):
        self.resources = []
        self.session_manager = session_manager

    def add_resource(self, resource: Resource):
        Log.p(f"Adding resource: {resource.type}")

        self.resources.append(resource)
        self.notify_session_manager(resource)

    def notify_session_manager(self, resource: Resource):
        self.session_manager.process_resource(resource)
