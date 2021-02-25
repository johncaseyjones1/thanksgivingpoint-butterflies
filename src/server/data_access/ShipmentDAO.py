import pymongo
import unittest
import json

from request.shipment import getShipmentRequest
from request.shipment import getShipmentsInRangeRequest
from request.shipment import insertShipmentRequest
from request.shipment import updateShipmentRequest

from response.shipment import getShipmentResponse
from response.shipment import getShipmentsInRangeResponse
from response.shipment import insertShipmentResponse
from response.shipment import updateShipmentResponse

class ShipmentDAO:

    # This function is for finding and returning all shipments from the MongoDB Database
    def getAllShipments(request):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["observatory"]
        col = db["shipment"]

        shipments = col.find()

        return shipments

    # This function is for finding and returning a list of shipments from the MongoDB Database that
    # fit within the range given  
    def getShipmentsInRange(request):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["observatory"]
        col = db["shipment"]

        greaterThan = "$gt"
        lessThan = "$lt"

        query = {
                "$and": [
                    {"date": { greaterThan : request.getDate1()}},
                    {"date": { lessThan : request.getDate2()}}
                ]
            }

        shipment = col.find(query)

        return getShipmentsInRangeResponse.GetShipmentsInRangeResponse(shipment)

    # This function is for finding and returning one shipment from the MongoDB Database
    def getOneShipment(request):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["observatory"]
        col = db["shipment"]

        query = {"_id": request.getID()}

        shipment = col.find_one(query)

        return getShipmentResponse.GetShipmentResponse(shipment)


    # This function is for inserting one observation into the MongoDB Database
    def insertOneShipment(request):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["observatory"]
        col = db["shipment"]

        # I don't set an ID here becasue MongoDB will create one for us and handle any clashing.
        shipment = {"speciesID": request.getSpeciesID(),
                    "dateEntered": request.getDateEntered(),
                    "origin": request.getOrigin(),
                    "quantity": request.getQuantity(),
                    "supplier": request.getSupplier(),
                    "emergedEarly": request.getEmergedEarly(),
                    "deadOnArrival": request.getDeadOnArrival(),
                    "failedToEmerge": request.getFailedToEmerge(),
                    "parasitized": request.getParasitized()}

        ID = col.insert_one(shipment).inserted_id

        return insertShipmentResponse.InsertShipmentResponse(ID)

    # This function updates a shipment that has already been entered to change previously
    # entered values or to add values contained in the ShipmentDataModel class
    def updateShipment(request):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["observatory"]
        col = db["shipment"]

        data = { $set: {"numGlued": request.getNumGlued(),
                "percentEmergence": request.getPercentEmergence(),
                "susNumReleased": request.getSusNumReleased()
                }}

        filter = {"_id": request.getShipmentID()}
        result = col.update_one(filter, data)
        message = "success"
        if result.modified_count != 1:
            message = "error"

        return updateShipmentResponse.UpdateShipmentResponse(message)