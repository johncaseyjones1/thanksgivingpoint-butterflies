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
from datetime import datetime as DT
from datetime import timedelta
from generators.worldGraphScript import MapGenerator

from response.longevity.GetLongevityResponse import GetLongevityResponse



class LongevityDAO:
    def getLongevityStillFlying(self):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["observatory"]
        col = db["longevity"]

        longestLiving = col.find_one({ "Probable_Longevity": 
                                        { "$not":  {"$gte": "na" } 
                                        }
                                    },{"Probable_Longevity": 1, "_id": 0}, sort=[("Probable_Longevity", pymongo.DESCENDING)])

        longestLivingTime = longestLiving["Probable_Longevity"]

        col = db["release"]

        today = DT.utcnow().now()
        sinceDay = today - timedelta(days = int(longestLivingTime))

        greaterThanOrEqual = "$gte"

        query = {
            "Date": { greaterThanOrEqual : sinceDay }
        }

        releasesSinceMaxDays = col.find(query)
        releaseList = list(releasesSinceMaxDays)
        goodReleasesList = []
        col = db["longevity"]

        for item in releaseList:
            longevitySpecific = col.find_one({"Scientific_name": item["Species"]}, {"Probable_Longevity": 1, "_id": 0})
            if longevitySpecific is not None:
                lifeSpan = longevitySpecific["Probable_Longevity"]
                if lifeSpan != 'na':
                    sinceDay = today - timedelta(days = int(lifeSpan))
                    if item["Date"] > sinceDay:
                        goodReleasesList.append(item)


        response = GetLongevityResponse(dumps(goodReleasesList))
        return response

    def getLongevityRecentReleases(self):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["observatory"]
        col = db["longevity"]

        longestLiving = col.find_one({ "Probable_Longevity": 
                                        { "$not":  {"$gte": "na" } 
                                        }
                                    },{"Probable_Longevity": 1, "_id": 0}, sort=[("Probable_Longevity", pymongo.DESCENDING)])

        longestLivingTime = longestLiving["Probable_Longevity"]

        col = db["release"]

        today = DT.utcnow().now()
        sinceDay = today - timedelta(days = int(longestLivingTime))

        greaterThanOrEqual = "$gte"

        query = {
            "Date": { greaterThanOrEqual : sinceDay }
        }

        releasesSinceMaxDays = col.find(query)
        releaseList = list(releasesSinceMaxDays)
        goodReleasesList = []
        col = db["longevity"]

        for item in releaseList:
            longevitySpecific = col.find_one({"Scientific_name": item["Species"]}, {"Probable_Longevity": 1, "_id": 0})
            if longevitySpecific is not None:
                lifeSpan = longevitySpecific["Probable_Longevity"]
                if lifeSpan != 'na':
                    sinceDay = today - timedelta(days = int(lifeSpan))
                    if item["Date"] > sinceDay:
                        goodReleasesList.append(item)

        pathToGraph = MapGenerator.generateGraph(goodReleasesList)

        #response = GetLongevityResponse(dumps(goodReleasesList))

        #return response
        return pathToGraph
        #return response