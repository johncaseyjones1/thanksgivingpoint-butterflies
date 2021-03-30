from excel2json import convert_from_file
import json
import pymongo
import os

dirname = os.path.dirname(__file__)
raw_data = os.path.join(dirname, 'raw_data/ButterflyMatrix.xls')
json_data = os.path.join(dirname, 'raw_data/ButterflySpecies.json')

# Change to the absolute path of this file on your machine
convert_from_file('/Users/bradyneeley/Bio465/thanksgivingpoint-butterflies/src/server/database_loaders/raw_data/ButterflyMatrix.xls')

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["observatory"]
col = db["butterfly_species"]

# Clear database to prevent duplicates
col.delete_many({})

with open('/Users/bradyneeley/Bio465/thanksgivingpoint-butterflies/src/server/database_loaders/raw_data/ButterflySpecies.json') as file: 
    file_data = json.load(file) 

col.insert_many(file_data)