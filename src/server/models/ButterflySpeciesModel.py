class ButterflySpecies:

    def __init__(self, id, tColor, bColor, num, place)
        self.speciesID = id
        self.topWingColor = tColor
        self.bottomWingColor = bColor
        self.size = num
        self.location = place

    def setSpeciesID(self, id):
        self.speciesID = id

    def getScientificName(self):
        return self.speciesID

    def setTopWingColor(self, tColor):
        self.topWingColor = tColor

    def getTopWingColor(self):
        return self.topWingColor

    def setBottomWingColor(self, bColor):
        self.bottomWingColor = bColor

    def getBottomWingColor(self):
        return self.bottomWingColor

    def setSize(self, num):
        self.size = num

    def getSize(self):
        return self.size

    def setLocation(self, place):
        self.location = place

    def getLocation(self):
        return self.location