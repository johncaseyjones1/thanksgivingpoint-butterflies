class ButterflySpeciesDAO:

    # This function is for finding and returning all butterflies from the MongoDB Database
    def getAllButterflies(request):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["observatory"]
        col = db["butterflySpecies"]

        butterflies = col.find()

        return butterflies


    # This function is for finding and returning a list of the current butterflies from the MongoDB Database  
    def getCurrentButterflies(request):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["observatory"]
        col = db["butterflySpecies"]

        greaterThan = "$gt"

        query = {"date": { greaterThan : request.getDate1()}}

        butterflies = col.find(query)

        return getCurrentButterfliesResponse.GetCurrentButterfliesResponse(butterflies)


    # This function is for finding and returning one butterfly from the MongoDB Database
    def getOneButterfly(request):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["observatory"]
        col = db["butterflySpecies"]

        #_id works here for getting one butterfly query, thats in this part of the table? No, ask how we'd like to best
        #go about that...
        query = {"_id": request.getID()}

        butterfly = col.find_one(query)

        return getOneButterflyResponse.GetOneButterflyResponse(butterfly)


    # This function is for inserting one butterfly species into the MongoDB Database
    def insertOneButterfly(request):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["observatory"]
        col = db["butterflySpecies"]

        # I don't set an ID here becasue MongoDB will create one for us and handle any clashing.
        observation = {"speciesID": request.speciesID,
                        "topWingColor": request.topWingColor,
                        "bottomWingColor": request.bottomWingColor,
                        "size": request.size,
                        "location": request.location}

        ID = col.insert_one(observation).inserted_id

        return insertOneButterflyResponse.InsertOneButterflyResponse(ID)

        
import pymongo
import unittest
import json
from bson.json_util import dumps

from request.butterfly_species import GetButterflySpeciesRequest
from response.butterfly_species import GetButterflySpeciesResponse

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

        #size = 0
        #for species in speciesFound:
        #    speciesList.append(species)
        #    size += 1
        
        #if size == 0:
        #    response.setResponse("nothing found!")
        #    return response

        response.setResponse(dumps(speciesList))
        return response

    def getAllSpecies():
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["observatory"]
        col = db["butterfly_species"]

        allSpecies = col.find({})
        speciesList = list(allSpecies)

        response = GetButterflySpeciesResponse.GetButterflySpeciesResponse()
        response.setResponse(dumps(speciesList))

        return response
