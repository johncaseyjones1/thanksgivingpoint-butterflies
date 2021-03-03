from excel2json import convert_from_file
import json
import pymongo

# Change to the absolute path of this file on your machine
convert_from_file('/home/caseyjones/github/thanksgivingpoint-butterflies/src/server/database_loaders/raw_data/ButterflyMatrix.xls')

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["observatory"]
col = db["butterfly_species"]

# Clear database to prevent duplicates
col.delete_many({})

with open('/home/caseyjones/github/thanksgivingpoint-butterflies/src/server/database_loaders/raw_data/ButterflySpecies.json') as file: 
    file_data = json.load(file) 

col.insert_many(file_data)