import pymongo
from bson.json_util import dumps
from bson.objectid import ObjectId
import dateutil.parser as parser
from datetime import datetime

from request.release import getReleaseRequest
from request.release import insertReleaseRequest
from request.release import updateReleaseRequest

from response.release import getReleaseResponse
from response.release import insertReleaseResponse
from response.release import updateReleaseResponse


class ReleaseDAO:

    def getAllReleases(request):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["observatory"]
        col = db["release"]
        
        releases = col.find({})        
        releaseList = list(releases)

        response = getReleaseResponse.GetReleaseResponse(dumps(releaseList))

        return response


    def getOneRelease(request):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["observatory"]
        col = db["release"]

        query = {"_id": request.getID()}

        release = col.find(query)

        return getReleaseResponse.GetReleaseResponse(release)

    def insertOneRelease(self, request):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["observatory"]
        col = db["release"]
        date = parser.parse(request.getDate())

        release = { "Date": date,
                    "Species": request.getSpecies(),
                    "Quantity": int(request.getCount())}
        
        ID = col.insert_one(release).inserted_id

        return insertReleaseResponse.InsertReleaseResponse("successfully submitted release")

    def updateRelease(request):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["observatory"]
        col = db["release"]

        data = { "$set": {"speciesID": request.getSpeciesID(),
                "count": request.getCount(),
                "releaseDate": request.getReleaseDate()
                }}
        filter = {"_id": request.getReleaseID()}
        result = col.update_one(filter, data)
        message = "success"
        if result.modified_count != 1:
            message = "error while updating release"
        
        return updateReleaseResponse.updateReleaseResponse(message)

    def deleteRelease(self, request):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["observatory"]
        col = db["release"]

        # I don't set an ID here becasue MongoDB will create one for us and handle any clashing.
        objectID = ObjectId(request.getReleaseID())
        filter = {"_id": objectID}

        resp = col.delete_one(filter)

        if resp.acknowledged == True:
            return insertReleaseResponse.InsertReleaseResponse("successfully deleted release")
        
        else:
            return insertReleaseResponse.InsertReleaseResponse("Could not delete release")