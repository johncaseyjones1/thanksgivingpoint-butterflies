import pymongo

from request.GetLocationRequest import getLocation
from response.GetLocationResponse import *


class LocationDAO:

    def getAllLocations():
            client = pymongo.MongoClient("mongodb://localhost:27017/")
            db = client["observatory"]
            col = db["butterfly_species"]

            allLocations = col.inventory.find( {}, { location: 1 } )

            locationsList = list(allLocations)

            response = getLocationResponse.getResponse()
            response.setResponse(dumps(allLocations))

            return response