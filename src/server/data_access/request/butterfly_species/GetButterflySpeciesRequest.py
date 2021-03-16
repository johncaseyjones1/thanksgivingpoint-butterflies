class GetButterflySpeciesRequest:
    def __init__(self, predictionRequest):
        self.size = predictionRequest["size"]
        self.eyespot = predictionRequest["eyespot"]
        self.pattern = predictionRequest["pattern"]
        self.wingShape = int(predictionRequest["wingShape"])
        self.primaryColor = predictionRequest["primaryColor"]
        self.secondaryColor = predictionRequest["secondaryColor"]

    def getSize(self):
        return self.size

    def getEyespot(self):
        return self.eyespot

    def getPattern(self):
        return self.pattern

    def getWingShape(self):
        return self.wingShape

    def getPrimaryColor(self):
        return self.primaryColor

    def getSecondaryColor(self):
        return self.secondaryColor

    