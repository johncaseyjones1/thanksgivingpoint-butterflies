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
