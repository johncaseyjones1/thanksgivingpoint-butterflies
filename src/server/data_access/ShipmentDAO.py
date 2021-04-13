import os
import sys
sys.path.append('../../')
import pymongo
from bson.json_util import dumps
import json
import csv
from bson.objectid import ObjectId
import dateutil.parser as parser
from datetime import datetime

from request.shipment import getShipmentRequest
from request.shipment import getShipmentsInRangeRequest
from request.shipment import insertShipmentRequest
from request.shipment import updateShipmentRequest

from response.shipment.getShipmentResponse import GetShipmentResponse
from response.shipment import getShipmentsInRangeResponse
from response.shipment import insertShipmentResponse
from response.shipment import updateShipmentResponse

class ShipmentDAO:

    # This function is for finding and returning all shipments from the MongoDB Database
    def getAllShipments(request):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["observatory"]
        col = db["shipment"]
        static_path=os.path.join(os.path.dirname(__file__), "../public")

        shipments = col.find({})        
        shipmentList = list(shipments)

        response = GetShipmentResponse(dumps(shipmentList))
        
        shipmentsNoID = col.find({},{"_id":0})   
        jsonFile = open(static_path + "/shipments/shipments.json", 'w')
        shipmentList = list(shipmentsNoID)

        for shipment in shipmentList:
            shipment["Date"] = shipment["Date"].strftime("%m/%d/%Y")

        json.dump(shipmentList, jsonFile)
        jsonFile.close()
        with open(static_path + "/shipments/shipments.json", 'r') as jsonFile:
            jsonData = json.load(jsonFile)

        
        csv_file = open(static_path + "/shipments/shipments.csv", 'w')

        csv_writer = csv.writer(csv_file)

        count = 0
        for shipment in jsonData:
            if count == 0:
                header = shipment.keys()
                csv_writer.writerow(header)
                count += 1
            
            csv_writer.writerow(shipment.values())
        
        csv_file.close()
        jsonFile.close()

        return response

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
    def insertOneShipment(self, request):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["observatory"]
        col = db["shipment"]
        date = parser.parse(request.getDate())

        # I don't set an ID here becasue MongoDB will create one for us and handle any clashing.
        shipment = {
                    "Date": date,
                    "Species": request.getSpecies(),
                    "Origin": request.getOrigin(),
                    "Quantity": int(request.getQuantity()),
                    "Supplier": request.getSupplier(),
                    "EmergedEarly": int(request.getEmergedEarly()),
                    "DOA": int(request.getDeadOnArrival()),
                    "FTE": int(request.getFailedToEmerge()),
                    "W": int(request.getWings()),
                    "Parasite": int(request.getParasitized())}

        ID = col.insert_one(shipment).inserted_id

        return insertShipmentResponse.InsertShipmentResponse("successfully submitted shipment")

    # This function updates a shipment that has already been entered to change previously
    # entered values or to add values contained in the ShipmentDataModel class
    def updateShipment(self, request):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["observatory"]
        col = db["shipment"]

        data = { "$set" : {"Species": request.getSpecies(),
                        "Date": datetime.utcfromtimestamp(int(request.getDate())/1000),
                        "Origin": request.getOrigin(),
                        "Quantity": int(request.getQuantity()),
                        "Supplier": request.getSupplier(),
                        "EmergedEarly": int(request.getEmergedEarly()),
                        "DOA": int(request.getDeadOnArrival()),
                        "FTE": int(request.getFailedToEmerge()),
                        "W": int(request.getWings()),
                        "Parasite": int(request.getParasitized())}
                }

        objectID = ObjectId(request.getShipmentID())

        filter = {"_id": objectID}
        result = col.update_one(filter, data)
        message = "success"
        if result.modified_count != 1:
            message = "error, modified {} shipment(s) using data {}".format(result.modified_count, data)

        return updateShipmentResponse.UpdateShipmentResponse(message)



    def deleteShipment(self, request):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["observatory"]
        col = db["shipment"]

        # I don't set an ID here becasue MongoDB will create one for us and handle any clashing.
        objectID = ObjectId(request.getShipmentID())
        filter = {"_id": objectID}

        resp = col.delete_one(filter)

        if resp.acknowledged == True:
            return insertShipmentResponse.InsertShipmentResponse("successfully deleted shipment")
        
        else:
            return insertShipmentResponse.InsertShipmentResponse("Could not delete shipment")