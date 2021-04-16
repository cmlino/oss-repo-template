from bson.objectid import ObjectId
from pymongo import MongoClient
from random import choice
import datetime
import pprint

client = MongoClient('localhost', 27017)
db = client.mongo_db_lab
collection = db["definitions"]

def random_word_requester():
    records_list = []

    for r in collection.find():
        records_list.append(r)

    selected = choice(records_list)

    pprint.pprint(selected)

    current_time = datetime.datetime.utcnow().isoformat()
    current_dates = []
    if 'dates' in selected.keys(): 
        current_dates = selected['dates']
    current_dates.append(current_time)
    id = ObjectId(selected['_id'])
    word = selected['word'] 

    print("Add date")
    collection.update_one({"word": word}, {"$set":{"dates": current_dates}})

    print("Added")
    pprint.pprint((collection.find_one({"word": word })))
    
if __name__ == "__main__":
    random_word_requester()


