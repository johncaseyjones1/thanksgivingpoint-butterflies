class ShipmentDataModel():

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
        

    def setShipmentID(shipmentID):
        self.shipmentID = shipmentID

    def setNumGlued(numGlued):
        self.numGlued = numGlued

    def setPercentEmergence(percentEmergence):
        self.percentEmergence = percentEmergence

    def setSusNumReleased(susNumReleased):
        self.susNumReleased = susNumReleased