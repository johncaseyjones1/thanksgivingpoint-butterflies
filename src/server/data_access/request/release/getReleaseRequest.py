class GetReleaseRequest:

    def __init__(self, ID, getAll):
        self.ID = ID
        self.getAll = getAll
    
    def getID(self):
        return self.ID

    def getAll(self):
        return self.getAll
    