

class InsertObservationRequest:
    def __init__(self, date, time, picturePath, speciesPrediction):
        self.date = date
        self.time = time
        self.picturePath = picturePath
        self.speciesPrediction = speciesPrediction

    def getDate(self):
        return self.date

    def getTime(self):
        return self.time

    def getPicturePath(self):
        return self.picturePath
    
    def getSpeciesPrediction(self):
        return self.speciesPrediction