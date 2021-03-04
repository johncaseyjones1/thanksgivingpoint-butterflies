class GetObservationRequest:

    def __init__(shipmentID, numGlued, percentEmergence, susNumReleased):
        self.shipmentID = shipmentID
        self.numGlued = numGlued
        self.percentEmergence = percentEmergence
        self.susNumReleased = susNumReleased

    def getShipmentID():
        return self.shipmentID

    def getNumGlued():
        return self.numGlued

    def getPercentEmergence():
        return self.percentEmergence

    def getSusNumReleased():
        return self.susNumReleased