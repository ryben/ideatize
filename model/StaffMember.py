from core.BaseSubscriber import BaseSubscriber
from model.Data import Staff, Role
from resource.Resource import Resource


class StaffMember(BaseSubscriber):
    name: str
    role: Role

    def __init__(self, staff_info: Staff, roles: list[Role]):
        self.name = staff_info.name

        for role in roles:
            if role.name == staff_info.role:
                self.role = role
                break

    def on_get_update(self, resource: Resource):
        if resource.type in self.role.inputs:
            print(resource.type)
