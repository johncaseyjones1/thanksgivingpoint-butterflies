class EditSpeciesRequest:
    
    def __init__(self, speciesID, scientificName, commonName, size, wingShape, primaryColor,
     secondaryColor, location, pattern, eyespot, hostPlant, quickFact, imagePath, sexuallyDimorphic):
        self.speciesID = speciesID
        self.scientificName = scientificName
        self.commonName = commonName
        self.size = size
        self.wingShape = wingShape
        self.primaryColor = primaryColor
        self.secondaryColor = secondaryColor
        self.location = location
        self.eyespot = eyespot
        self.hostPlant = hostPlant
        self.quickFact = quickFact
        self.imagePath = imagePath
        self.pattern = pattern
        self.sexuallyDimorphic = sexuallyDimorphic

    def getSpeciesID(self):
        return self.speciesID

    def getScientificName(self):
        return self.scientificName

    def getCommonName(self):
        return self.commonName

    def getSize(self):
        return self.size

    def getWingShape(self):
        return self.wingShape

    def getPrimaryColor(self):
        return self.primaryColor

    def getSecondaryColor(self):
        return self.secondaryColor

    def getLocation(self):
        return self.location

    def getEyespot(self):
        return self.eyespot

    def getHostPlant(self):
        return self.hostPlant

    def getQuickFact(self):
        return self.quickFact

    def getSexuallyDimorphic(self):
        return self.sexuallyDimorphic

    def getImagePath(self):
        return self.imagePath
    
    def setImagePath(self, imagePath):
        self.imagePath = imagePath

    def getPattern(self):
        return self.pattern