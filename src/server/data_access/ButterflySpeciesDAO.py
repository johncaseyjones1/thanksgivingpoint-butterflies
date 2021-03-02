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
        lessThan = "$lt"

        #GET RID OF THE LESS THAN QUERY HERE???
        query = {
                "$and": [
                    {"date": { greaterThan : request.getDate1()}},
                    {"date": { lessThan : request.getDate2()}}
                ]
            }

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