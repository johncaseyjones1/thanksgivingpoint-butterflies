import pymongo
import os
import sys
sys.path.append('../')
from generators.worldGraphScript import MapGenerator
from bson.json_util import dumps
from request.butterfly_species.GetLocationRequest import getLocationRequest
from response.butterfly_species.GetLocationResponse import GetLocationResponse


class LocationDAO:

    def getAllLocations(self):
            client = pymongo.MongoClient("mongodb://localhost:27017/")
            db = client["observatory"]
            col = db["butterfly_species"]

            allLocations = col.inventory.find( {}, { "Location": 1 } )

            locationsList = list(allLocations)
            pathToMap = MapGenerator.generateMap(locationsList)

            #response = GetLocationResponse.getResponse()
            #response.setResponse(dumps(locationsList)) returns file path instead

            return pathToMap