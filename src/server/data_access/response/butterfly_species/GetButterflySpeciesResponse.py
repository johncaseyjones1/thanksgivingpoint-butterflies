class GetButterflySpeciesResponse:
    def __init__(self):
        self.response = None

    def getResponse(self):
        return self.response

    def setResponse(self, response):
        self.response = response

    def __dict__(self):
        return {"speciesPredictions": self.response}

    