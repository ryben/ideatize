class Resource:
    type: str
    content: str

    def __init__(self, resource_type: str, content: str):
        self.type = resource_type
        self.content = content
