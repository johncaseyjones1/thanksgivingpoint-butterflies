

class InsertObservationRequest:
    def __init__(self, dateTime, picturePath, speciesPrediction, commonName):
        self.dateTime = dateTime
        self.picturePath = picturePath
        self.speciesPrediction = speciesPrediction
        self.commonName = commonName

    def getDateTime(self):
        return self.dateTime

    def setDateTime(self, dateTime):
        self.dateTime = dateTime

    def getPicturePath(self):
        return self.picturePath
    
    def getSpeciesPrediction(self):
        return self.speciesPrediction

    def getCommonName(self):
        return self.commonName