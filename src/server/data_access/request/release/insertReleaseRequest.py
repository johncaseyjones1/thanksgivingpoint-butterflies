class InsertReleaseRequest:

    def __init__(self, species, count, date):
        self.species = species
        self.count = count
        self.date = date

    def getSpecies(self):
        return self.species

    def getCount(self):
        return self.count

    def getDate(self):
        return self.date

    