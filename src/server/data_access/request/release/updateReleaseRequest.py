class updateReleaseRequest:

    def __init__(self, speciesID, count, releaseDate):
        self.speciesID = speciesID
        self.count = count
        self.releaseDate = releaseDate

    def getSpeciesID(self):
        return self.speciesID

    def getCount(self):
        return self.count

    def getReleaseDate(self):
        return self.releaseDate