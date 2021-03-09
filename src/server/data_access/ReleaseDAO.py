import pymongo
import unittest
import json

from request.release import GetReleaseRequest
from request.release import InsertReleaseRequest
from request.release import UpdateReleaseRequest

from response.release import GetReleaseResponse
from response.release import InsertReleaseResponse
from response.release import UpdateReleaseResponse


class ReleaseDAO:

    def getAllReleases(request):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["observatory"]
        col = db["release"]
        
        releases = col.find()

        return releases

    def getOneRelease(request):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["observatory"]
        col = db["release"]

        query = {"_id": request.getID()}

        release = col.find(query)

        return getReleaseResponse.GetReleaseResponse(release)

    def insertOneRelease(request):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["observatory"]
        col = db["release"]

        release = {"speciesID": request.getSpeciesID(),
                    "count": request.getCount(),
                    "releaseDate": request.getReleaseDate()}
        
        ID = col.insert_one(release).inserted_id

        return insertReleaseResponse.InsertReleaseResponse(ID)

    def updateRelease(request):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["observatory"]
        col = db["release"]

        data = { $set: {"speciesID": request.getSpeciesID(),
                "count": request.getCount(),
                "releaseDate": request.getReleaseDate()
                }}
        filter = {"_id": request.getReleaseID()}
        result = col.update_one(filter, data)
        message = "success"
        if result.modified_count != 1:
            message = "error while updating release"
        
        return updateReleaseResponse.updateReleaseResponse(message)

    