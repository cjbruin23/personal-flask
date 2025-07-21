class Community:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def createJsonObj(self):
        x = {
            "id": self.id,
            "name": self.name,
        }

        return x