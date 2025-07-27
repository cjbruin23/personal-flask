class Community:
    def __init__(self, id, name, size, gdp):
        self.id = id
        self.name = name
        self.size = size
        self.gdp = gdp

    def create_json_obj(self):
        x = {
            "id": self.id,
            "name": self.name,
            "size": self.size,
            "gdp": self.gdp,
        }

        return x