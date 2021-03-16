from excel2json import convert_from_file
import json
import pymongo
from datetime import datetime

# Change to the absolute path of this file on your machine
convert_from_file('/Users/emmepratt/Downloads/Butterfly_Biosphere/thanksgivingpoint-butterflies/src/server/database_loaders/raw_data/shipments.xls')

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["observatory"]
col = db["shipment"]

# Clear database to prevent duplicates
col.delete_many({})

with open('/Users/emmepratt/Downloads/Butterfly_Biosphere/thanksgivingpoint-butterflies/src/server/database_loaders/raw_data/shipments.json') as file: 
    file_data = json.load(file) 
    for line in file_data:
        excel_date = int(line["Date"])
        dt = datetime.fromordinal(datetime(1900, 1, 1).toordinal() + excel_date - 2)
        line["Date"] = dt
        if line["EmergedEarly"] == "":
            line["EmergedEarly"] = 0
        if line["DOA"] == "":
            line["DOA"] = 0
        if line["FTE"] == "":
            line["FTE"] = 0
        if line["W"] == "":
            line["W"] = 0
        if line["Parasite"] == "":
            line["Parasite"] = 0

    col.insert_many(file_data)