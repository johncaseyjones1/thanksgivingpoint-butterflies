class InsertShipmentRequest:
    
    def __init__(self, date, species, origin, quantity, supplier, emergedEarly, deadOnArrival, failedToEmerge=0, parasitized=0):
        self.date = date
        self.species = species
        self.origin = origin
        self.quantity = quantity
        self.supplier = supplier
        self.emergedEarly = emergedEarly
        self.deadOnArrival = deadOnArrival
        self.failedToEmerge = failedToEmerge
        self.parasitized = parasitized

    def getDate(self):
        return self.date

    def getSpecies(self):
        return self.species

    def getOrigin(self):
        return self.origin

    def getQuantity(self):
        return self.quantity

    def getSupplier(self):
        return self.supplier

    def getEmergedEarly(self):
        return self.emergedEarly

    def getDeadOnArrival(self):
        return self.deadOnArrival

    def getFailedToEmerge(self):
        return self.failedToEmerge

    def getParasitized(self):
        return self.parasitized