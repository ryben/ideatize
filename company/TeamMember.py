from company import Role


class TeamMember:
    name: str
    role: Role

    def __init__(self, name: str, role: Role):
        self.name = name
        self.role = role
