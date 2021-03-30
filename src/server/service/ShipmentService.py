
import sys, os
lib_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data_access'))
sys.path.append(lib_path)
from ShipmentDAO import ShipmentDAO

class EditShipment:
    
    @staticmethod
    def editOneShipment(request):
        shipmentDAO = ShipmentDAO()
        return shipmentDAO.updateShipment(request)

class DeleteShipment:
    
    @staticmethod
    def deleteOneShipment(request):
        shipmentDAO = ShipmentDAO()
        return shipmentDAO.deleteShipment(request)

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