class Select:
    def __init__(self, values, table):
        self.values = values
        self.table = table
    def __str__(self):
        stringBuilder = 'SELECT '
        stringBuilder += f" {self.values}"
        stringBuilder += f' FROM {self.table}'
        return stringBuilder
