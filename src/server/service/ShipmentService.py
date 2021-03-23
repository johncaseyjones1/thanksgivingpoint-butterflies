
import sys, os
parent_dir = os.getcwd() # find the path to module a
# Then go up one level to the common parent directory
path = os.path.dirname(parent_dir)
# Add the parent to sys.pah
sys.path.insert(1, "/Users/bradyneeley/Bio465/thanksgivingpoint-butterflies/src/server/data_access/")
from ShipmentDAO import ShipmentDAO


class InsertShipment:

    @staticmethod
    def insertOneShipment(request):
        shipmentDAO = ShipmentDAO()
        return shipmentDAO.insertOneShipment(request)

class GetAllShipments:

    @staticmethod
    def getAllShipments():
        shipmentDAO = ShipmentDAO()
        return shipmentDAO.getAllShipments()