from pymongo import MongoClient

# Инициализация клиента - MongoDB
client = MongoClient('localhost', 27017)

# Создание таблицы - Data
db = client['Data']

# Создание коллекций внутри таблицы
restaurants_collection = db['Restaurants']
cafes_collection = db['Cafes']
bars_collection = db['Bars']
favorites_collection = db['Favorites']


# Вставить элемент в коллекцию
def insert_document(collection, data):
    return collection.insert_one(data).inserted_id


# Найти элемент в коллекции
def find_document(collection, elements, multiple=False):
    if multiple:
        results = collection.find(elements)
        return [r for r in results]
    else:
        return collection.find_one(elements)


# Обновить элемент в коллекции
def update_document(collection, query_elements, new_values):
    collection.update_one(query_elements, {'$set': new_values})


# Удалить элемент из коллекции
def delete_document(collection, query):
    collection.delete_one(query)


# Вернуть все данные из коллекции
def list_all(collection):
    return list(collection.find({}))
