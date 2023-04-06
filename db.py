from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['Data']
restaurants_collection = db['Restaurants']
cafes_collection = db['Cafes']
bars_collection = db['Bars']
favorites_collection = db['Favorites']


def insert_document(collection, data):
    return collection.insert_one(data).inserted_id


def find_document(collection, elements, multiple=False):
    if multiple:
        results = collection.find(elements)
        return [r for r in results]
    else:
        return collection.find_one(elements)


def update_document(collection, query_elements, new_values):
    collection.update_one(query_elements, {'$set': new_values})


def delete_document(collection, query):
    collection.delete_one(query)
