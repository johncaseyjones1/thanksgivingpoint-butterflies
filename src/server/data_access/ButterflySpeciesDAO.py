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

from request.butterfly_species import GetButterflySpeciesRequest
from response.butterfly_species import GetButterflySpeciesResponse
from response.butterfly_species import insertButterflySpeciesResponse
from response.shipment import insertShipmentResponse

class ButterflySpeciesDAO:
    def getManySpecies(self, request):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["observatory"]
        col = db["butterfly_species"]
        
        size = {"Size": request.size}
        eyespot = {"Eyespot": request.eyespot}
        pattern = {"Pattern": request.pattern}
        primaryColor = {"PrimaryColor": request.primaryColor}
        secondaryColor = {"SecondaryColor": request.secondaryColor}
        wingshape = {"WingShape": request.wingShape}
        query = {
            "$or": [
                {"$and": [
                    eyespot,
                    pattern,
                    primaryColor,
                    secondaryColor,
                    wingshape
                ]},
                {"$and": [
                    size,
                    pattern,
                    primaryColor,
                    secondaryColor,
                    wingshape
                ]},
                {"$and": [
                    size,
                    eyespot,
                    primaryColor,
                    secondaryColor,
                    wingshape
                ]},
                {"$and": [
                    size,
                    eyespot,
                    pattern,
                    secondaryColor,
                    wingshape
                ]},
                {"$and": [
                    size,
                    eyespot,
                    pattern,
                    primaryColor,
                    wingshape
                ]},
                {"$and": [
                    size,
                    eyespot,
                    pattern,
                    primaryColor,
                    secondaryColor
                ]},
                {"$and": [
                    size,
                    eyespot,
                    pattern,
                    primaryColor,
                    secondaryColor,
                    wingshape
                ]}
            ]
        }

            

        speciesFound = col.find(query)
        speciesList = list(speciesFound)
        response = GetButterflySpeciesResponse.GetButterflySpeciesResponse()

        response.setResponse(dumps(speciesList))
        return response

    def getAllSpecies(self):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["observatory"]
        col = db["butterfly_species"]
        static_path=os.path.join(os.path.dirname(__file__), "../public")

        allSpecies = col.find({})
        speciesList = list(allSpecies)

        response = GetButterflySpeciesResponse.GetButterflySpeciesResponse()
        response.setResponse(dumps(speciesList))

        speciesNoID = col.find({},{"_id":0})  
        speciesList = list(speciesNoID)

        jsonFile = open(static_path + "/butterfly_species/butterfly_species.json", 'w')
        json.dump(speciesList, jsonFile)
        jsonFile.close()

        with open(static_path + "/butterfly_species/butterfly_species.json", 'r') as jsonFile:
            jsonData = json.load(jsonFile)


        csv_file = open(static_path + "/butterfly_species/butterfly_species.csv", 'w')

        csv_writer = csv.writer(csv_file)

        count = 0
        for species in jsonData:
            if count == 0:
                header = species.keys()
                csv_writer.writerow(header)
                count += 1
            
            csv_writer.writerow(species.values())
        
        csv_file.close()
        jsonFile.close()

        return response


    # This function is for inserting one butterfly species into the MongoDB Database
    def insertOneSpecies(self, request):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["observatory"]
        col = db["butterfly_species"]

        # I don't set an ID here becasue MongoDB will create one for us and handle any clashing.
        species = {"Species": request.getScientificName(),
                        "CommonName": request.getCommonName(),
                        "PrimaryColor": request.getPrimaryColor(),
                        "SecondaryColor": request.getSecondaryColor(),
                        "WingShape": int(request.getWingShape()),
                        "Pattern": request.getPattern(),
                        "Eyespot": request.getEyespot(),
                        "Size": request.getSize(),
                        "Location": request.getLocation(),
                        "ImagePath": request.getImagePath(),
                        "QuickFact": request.getQuickFact(),
                        "CaterpillarHostPlants": request.getHostPlant(),
                        "SexuallyDimorphic": request.getSexuallyDimorphic(),}

        col.insert_one(species)

        return insertButterflySpeciesResponse.InsertButterflySpeciesResponse("success")


    def editOneSpecies(self, request):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["observatory"]
        col = db["butterfly_species"]

        data = { "$set": 
                    {"Species": request.getScientificName(),
                    "CommonName": request.getCommonName(),
                    "PrimaryColor": request.getPrimaryColor(),
                    "SecondaryColor": request.getSecondaryColor(),
                    "WingShape": int(request.getWingShape()),
                    "Pattern": request.getPattern(),
                    "Eyespot": request.getEyespot(),
                    "Size": request.getSize(),
                    "Location": request.getLocation(),
                    "ImagePath": request.getImagePath(),
                    "QuickFact": request.getQuickFact(),
                    "CaterpillarHostPlants": request.getHostPlant(),
                    "SexuallyDimorphic": request.getSexuallyDimorphic()
                    } 
                }

        objectID = ObjectId(request.getSpeciesID())
        
        filter = {"_id": objectID}
        result = col.update_one(filter, data)
        message = "success"
        if result.modified_count != 1:
            message = "error, modified {} species using data {}".format(result.modified_count, data)


        return insertButterflySpeciesResponse.InsertButterflySpeciesResponse(message)



    def deleteSpecies(self, request):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["observatory"]
        col = db["butterfly_species"]

        # I don't set an ID here becasue MongoDB will create one for us and handle any clashing.
        objectID = ObjectId(request.getSpeciesID())
        filter = {"_id": objectID}

        resp = col.delete_one(filter)

        if resp.acknowledged == True:
            return insertShipmentResponse.InsertShipmentResponse("successfully deleted species")
        
        else:
            return insertShipmentResponse.InsertShipmentResponse("Could not delete species")
