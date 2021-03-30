from excel2json import convert_from_file
from bson.json_util import _json_convert, dumps
import json
import pymongo

from datetime import datetime
import os

dirname = os.path.dirname(__file__)
raw_data = os.path.join(dirname, 'raw_data/releases.xls')
json_data = os.path.join(dirname, 'raw_data/releases.json')
converted_data = os.path.join(dirname, 'raw_data/releases_converted.json')

convert_from_file(raw_data)

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["observatory"]
col = db["release"]

# Clear database to prevent duplicates
col.delete_many({})

with open(json_data) as file: 
    file_data = json.load(file) 
    dictList = []
    for line in file_data:
        #excel_date = int(line["Date"])
        #dt = datetime.fromordinal(datetime(1900, 1, 1).toordinal() + excel_date - 2)
        #line["Date"] = dt
        for item in line:
            if line[item] != 0 and item != "Date" and item != "Sum":
                excel_date = int(line["Date"])
                dt = datetime.fromordinal(datetime(1900, 1, 1).toordinal() + excel_date - 2)
                tempDict = {
                    "Date": dt,
                    "Species": item,
                    "Quantity": line[item]
                }
                dictList.append(tempDict)

    #json_converted = dumps(dictList)

col.insert_many(dictList)