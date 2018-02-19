from pymongo import MongoClient
import json
import os
from auth import MONGODB_URI

DB_NAME = 'day30bootcampflask'
COLLECTION_NAME = 'myFirstMDB'

FIELDS = {'first_name': True, 'last_name': True, 'dob': True, 'nationality': True, '_id': False}

with MongoClient(MONGODB_URI) as conn:
    collection = conn[DB_NAME][COLLECTION_NAME]
    
    collection.insert({ 'first_name': 'Annie', 'last_name': 'Person', 'nationality': 'Australian'})
    
    peeps = collection.find(projection=FIELDS)
    for doc in peeps:
        print(doc)