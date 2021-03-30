class UpdateShipmentRequest:

    def __init__(self, shipmentID, date, species, origin, quantity, supplier, emergedEarly, deadOnArrival, failedToEmerge, wings, parasitized):
        self.shipmentID = shipmentID
        self.date = date
        self.species = species
        self.origin = origin
        self.quantity = quantity
        self.supplier = supplier
        self.emergedEarly = emergedEarly
        self.deadOnArrival = deadOnArrival
        self.failedToEmerge = failedToEmerge
        self.wings = wings
        self.parasitized = parasitized

    def getShipmentID(self):
        return self.shipmentID

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

    def getWings(self):
         return self.wings

    def getParasitized(self):
        return self.parasitized