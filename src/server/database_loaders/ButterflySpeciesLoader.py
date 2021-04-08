from excel2json import convert_from_file
import json
import pymongo
import os

dirname = os.path.dirname(__file__)
raw_data = os.path.join(dirname, 'raw_data/ButterflyMatrix.xls')
json_data = os.path.join(dirname, 'raw_data/ButterflySpecies.json')

convert_from_file(raw_data)

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["observatory"]
col = db["butterfly_species"]

# Clear database to prevent duplicates
col.delete_many({})

with open(json_data) as file: 
    file_data = json.load(file) 

col.insert_many(file_data)