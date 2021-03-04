

class InsertObservationRequest:
    def __init__(self, dateTime, picturePath, speciesPrediction):
        self.dateTime = dateTime
        self.picturePath = picturePath
        self.speciesPrediction = speciesPrediction

    def getDateTime(self):
        return self.dateTime

    def setDateTime(self, dateTime):
        self.dateTime = dateTime

    def getPicturePath(self):
        return self.picturePath
    
    def getSpeciesPrediction(self):
        return self.speciesPrediction