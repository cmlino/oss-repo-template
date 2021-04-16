from bson.objectid import ObjectId
from pymongo import MongoClient
import pprint
client = MongoClient('localhost', 27017)
db = client.mongo_db_lab
collection = db.definitions

if __name__ == '__main__':
    

    # Fetch all records
    print("Fetch all records")
    for definition in collection.find():
        pprint.pprint(definition)
    
    # Fetch one record
    print("\n Fetch one record")
    pprint.pprint(collection.find_one())

    # Fetch a specifc record
    pprint.pprint(collection.find_one({"word": "Bulk"}))

    # Fetch a record by oject id
    pprint.pprint(collection.find_one({"_id": ObjectId("56fe9e22bad6b23cde07b8ce")}))

    # Insert a new record
    pprint.pprint(collection.insert_one({"word": "Orange", "definition": "Color of a nice sunset"}))
