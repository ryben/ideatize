class Resource:
    type: str
    content: str

    def __init__(self, type: str, content: str):
        self.type = type
        self.content = content
