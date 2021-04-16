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
    
    print("\n\n")

    # Fetch one record
    print("Fetch one record (random)")
    pprint.pprint(collection.find_one())

    print("\n\n")
    print("Fetch a specifc record (word: bulk)")
    pprint.pprint(collection.find_one({"word": "Bulk"}))

    print("\n\n")

    print("Fetch a record by oject id")
    pprint.pprint(collection.find_one({"_id": ObjectId("56fe9e22bad6b23cde07b8ce")}))

    print("\n\n")

    # Insert a new record
    collection.insert_one({"word": "Orange", "definition": "Color of a nice sunset"})
    pprint.pprint(collection.find_one({"word": "Orange"}))
