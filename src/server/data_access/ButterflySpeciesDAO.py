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
        
        #query = {"$and": [{"Size": "S"}, {"Eyespot": "N"}, {"Pattern": "Veination"}, {"PrimaryColor": "Orange"}, {"SecondaryColor": "Black"}, {"WingShape": 2}]}


        query = {
            "$and": [
                  {"Size": request.size},
                  {"Eyespot": request.eyespot},
                  {"Pattern": request.pattern},
                  {"PrimaryColor": request.primaryColor},
                  {"SecondaryColor": request.secondaryColor},
                  {"WingShape": request.wingShape}
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

        allSpecies = col.find({})
        speciesList = list(allSpecies)

        response = GetButterflySpeciesResponse.GetButterflySpeciesResponse()
        response.setResponse(dumps(speciesList))

        return response


    # This function is for inserting one butterfly species into the MongoDB Database
    def insertOneSpecies(self, request):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["observatory"]
        col = db["butterfly_species"]

        # I don't set an ID here becasue MongoDB will create one for us and handle any clashing.
        observation = {"Species": request.getScientificName(),
                        "CommonName": request.getCommonName(),
                        "PrimaryColor": request.getPrimaryColor(),
                        "SecondaryColor": request.getSecondaryColor(),
                        "WingShape": int(request.getWingShape()),
                        "Pattern": request.getPattern(),
                        "Eyespot": request.getEyespot(),
                        "Size": request.getSize(),
                        "Location": request.getLocation(),
                        "ImagePath": request.getImagePath(),
                        "Quick Fact": request.getQuickFact(),
                        "Caterpillar Host Plants": request.getHostPlant(),
                        "Sexually Dimorphic": request.getSecondaryColor(),}

        col.insert_one(observation)

        return insertButterflySpeciesResponse.InsertButterflySpeciesResponse("success")


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
