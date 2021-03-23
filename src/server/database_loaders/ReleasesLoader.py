from excel2json import convert_from_file
import json
import pymongo

from datetime import datetime
import os

dirname = os.path.dirname(__file__)
raw_data = os.path.join(dirname, 'raw_data/releases.xls')
json_data = os.path.join(dirname, 'raw_data/releases.json')

# Change to the absolute path of this file on your machine
convert_from_file(raw_data)

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["observatory"]
col = db["releasen"]

# Clear database to prevent duplicates
col.delete_many({})

with open(json_data) as file: 
    file_data = json.load(file) 
    for line in file_data:
        excel_date = int(line["Date"])
        dt = datetime.fromordinal(datetime(1900, 1, 1).toordinal() + excel_date - 2)
        line["Date"] = dt

col.insert_many(file_data)