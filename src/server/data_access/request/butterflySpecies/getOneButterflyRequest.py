class GetOneButterflyRequest:
    def __init__(self, ID, getAll):
        self.ID = ID
        self.getAll = getAll

    def getID(self):
        return self.ID

    def getGetAll(self):
        return self.getAll