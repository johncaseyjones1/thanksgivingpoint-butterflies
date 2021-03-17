class InsertObservationRequest:
    def __init__(self, id, tWingColor, bWingColor, size, location):
        self.speciesID = id
        self.topWingColor = tWingColor
        self.bottomWingColor = bWingColor
        self.size = size
        self.location = location

    def getSpeciesID(self):
        return self.speciesID

    def getTopWingColor(self):
        return self.topWingColor

    def getBottomWingColor(self):
        return self.bottomWingColor

    def getSize(self):
        return self.size

    def getLocation(self):
        return self.location