class GetObservationRequest:

    def __init__(self, shipmentID, speciesID, dateEntered, origin, quantity, supplier, emergedEarly, deadOnArrival, failedToEmerge, parasitized):
        self.shipmentID = shipmentID
        self.speciesID = speciesID
        self.dateEntered = dateEntered
        self.origin = origin
        self.quantity = quantity
        self.supplier = supplier
        self.emergedEarly = emergedEarly
        self.deadOnArrival = deadOnArrival
        self.failedToEmerge = failedToEmerge
        self.parasitized = parasitized

    def getShipmentID():
        return self.shipmentID

    def getSpeciesID():
        return self.speciesID

    def getDateEntered():
        return self.dateEntered

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