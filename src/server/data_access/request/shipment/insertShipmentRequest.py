class InsertShipmentRequest:
    
    def __init__(self, date, species, origin, quantity, supplier, emergedEarly, deadOnArrival, failedToEmerge=0, parasitized=0):
        self.date = date
        self.species = species
        self.origin = origin
        self.quantity = quantity
        self.supplier = supplier
        self.emergedEarly = emergedEarly
        self.deadOnArrival = deadOnArrival

    def getDate():
        return self.dateEntered

    def getSpecies():
        return self.species

    def getOrigin():
        return self.origin

    def getQuantity():
        return self.quantity

    def getSupplier():
        return self.supplier

    def getEmergedEarly():
        return self.emergedEarly

    def getDeadOnArrival():
        return self.deadOnArrival

    def getFailedToEmerge():
        return self.failedToEmerge

    def getParasitized():
        return self.parasitized