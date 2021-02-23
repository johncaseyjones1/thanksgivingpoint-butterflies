import pymongo
import unittest
import json

from request.observation import getObservationRequest
from response.observation import getObservationResponse
from request.observation import getObservationsInRangeRequest
from response.observation import getObservationsInRangeResponse
from response.observation import insertObservationResponse
from request.observation import insertObservationRequest

class ObservationDAO:

    # This function is for finding and returning all observations from the MongoDB Database
    def getAllObservations(request):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["observatory"]
        col = db["observation"]

        observations = col.find()

        return observations


    # This function is for finding and returning a list of observations from the MongoDB Database that
    # fit within the range given  
    def getObservationsInRange(request):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["observatory"]
        col = db["observation"]

        greaterThan = "$gt"
        lessThan = "$lt"

        query = {
                "$and": [
                    {"date": { greaterThan : request.getDate1()}},
                    {"date": { lessThan : request.getDate2()}}
                ]
            }

        observation = col.find(query)

        return getObservationsInRangeResponse.GetObservationsInRangeResponse(observation)


    # This function is for finding and returning one observation from the MongoDB Database
    def getOneObservation(request):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["observatory"]
        col = db["observation"]

        query = {"_id": request.getID()}

        observation = col.find_one(query)

        return getObservationResponse.GetObservationResponse(observation)


    # This function is for inserting one observation into the MongoDB Database
    def insertOneObservation(request):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["observatory"]
        col = db["observation"]

        # I don't set an ID here becasue MongoDB will create one for us and handle any clashing.
        observation = {"date": request.date,
                        "time": request.time,
                        "picture": request.picturePath}

        ID = col.insert_one(observation).inserted_id

        return insertObservationResponse.InsertObservationResponse(ID)



########## TESTS #############

class UnitTests(unittest.TestCase):

    def setUp(self):
        
        return super().setUp()


    # Test insertOneObservation
    def testInsert(self):
        request = insertObservationRequest.InsertObservationRequest("test", "test", "test")
        response = ObservationDAO.insertOneObservation(request=request)

        assert response.getMessage() is not None

    # Test getOneObservation
    def testFindOne(self):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["observatory"]
        col = db["observation"]

        col.insert_one({"_id": "test",
                        "date": "test",
                        "time": "test",
                        "picture": "test"})

        request = getObservationRequest.GetObservationRequest("test", False)
        response = ObservationDAO.getOneObservation(request=request)

        assert response.getResponse()["_id"] == "test"

    # Test getObservationsInRange
    def testFindInRange(self):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["observatory"]
        col = db["observation"]

        # Test dates
        col.insert_one({"_id": "test1",
                        "date": "2021/01/01",
                        "time": "00:00:00",
                        "picture": "test"})

        col.insert_one({"_id": "test2",
                        "date": "2021/01/02",
                        "time": "00:00:00",
                        "picture": "test"})

        col.insert_one({"_id": "test3",
                        "date": "2021/01/03",
                        "time": "00:00:00",
                        "picture": "test"})

        col.insert_one({"_id": "test4",
                        "date": "2021/01/04",
                        "time": "00:00:00",
                        "picture": "test"})

        col.insert_one({"_id": "test5",
                        "date": "2021/01/05",
                        "time": "00:00:00",
                        "picture": "test"})

        col.insert_one({"_id": "test6",
                        "date": "2021/01/06",
                        "time": "00:00:00",
                        "picture": "test"})

        request = getObservationsInRangeRequest.GetObservationsInRangeRequest("2021/01/02", "2021/01/05")
        response = ObservationDAO.getObservationsInRange(request=request)

        responseCheck = ""

        for doc in response.getObservations():
            responseCheck += json.dumps(doc)
            
        assert responseCheck == '{"_id": "test3", "date": "2021/01/03", "time": "00:00:00", "picture": "test"}{"_id": "test4", "date": "2021/01/04", "time": "00:00:00", "picture": "test"}'



    def tearDown(self):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["observatory"]
        col = db["observation"]

        query = {"picture": "test"}

        col.delete_many(query)

        return super().tearDown()

if __name__ == '__main__':
    unittest.main()