

class InsertObservationRequest:
    def __init__(self, date, time, picturePath):
        self.date = date
        self.time = time
        self.picturePath = picturePath

    def getDate(self):
        return self.date

    def getTime(self):
        return self.time

    def getPicturePath(self):
        return self.picturePath