from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from db import insert_document, find_document, update_document, delete_document
from db import restaurants_collection, bars_collection, cafes_collection, favorites_collection
from db import list_all


# Инициализация приложения
app = FastAPI()


# Получить из коллекции определенный объект
@app.get("/v1/{collection}/{item}")
def get_place(collection: str, item: str):
    try:
        if collection == 'favorites':
            favorite = find_document(favorites_collection, {'name': f'{item}'})
            return JSONResponse(status_code=200, content=favorite)
        elif collection == 'bars':
            bar = find_document(bars_collection, {'name': f'{item}'})
            return JSONResponse(status_code=200, content=bar)
        elif collection == 'cafes':
            cafe = find_document(cafes_collection, {'name': f'{item}'})
            return JSONResponse(status_code=200, content=cafe)
        elif collection == 'restaurants':
            restaurant = find_document(restaurants_collection, {'name': f'{item}'})
            return JSONResponse(status_code=200, content=restaurant)
    except Exception as ex:
        raise HTTPException(status_code=500, detail=ex)


# Добавить данные в коллекцию
@app.post("/v1/{collection}")
def add_place(collection: str, data: dict):
    try:
        if collection == 'favorites':
            favorite = insert_document(favorites_collection, data)
            return JSONResponse(status_code=200, content=favorite)
        elif collection == 'bars':
            bar = insert_document(bars_collection, data)
            return JSONResponse(status_code=200, content=bar)
        elif collection == 'cafes':
            cafe = insert_document(cafes_collection, data)
            return JSONResponse(status_code=200, content=cafe)
        elif collection == 'restaurants':
            restaurant = insert_document(restaurants_collection, data)
            return JSONResponse(status_code=200, content=restaurant)
    except Exception as ex:
        raise HTTPException(status_code=500, detail=ex)


# Обновить данные в коллекции по id
@app.put("/v1/{collection}/{_id}")
def update_place(collection: str, _id: int, data: dict):
    try:
        if collection == 'favorites':
            favorite = update_document(favorites_collection, {'_id': _id}, data)
            return JSONResponse(status_code=200, content=favorite)
        elif collection == 'bars':
            bar = update_document(bars_collection, {'_id': _id}, data)
            return JSONResponse(status_code=200, content=bar)
        elif collection == 'cafes':
            cafe = update_document(cafes_collection, {'_id': _id}, data)
            return JSONResponse(status_code=200, content=cafe)
        elif collection == 'restaurants':
            restaurant = update_document(restaurants_collection, {'_id': _id}, data)
            return JSONResponse(status_code=200, content=restaurant)
    except Exception as ex:
        raise HTTPException(status_code=500, detail=ex)


# Удалить объект из коллекции по id
@app.delete("/v1/{collection}/{_id}")
def delete_place(collection: str, _id: int):
    try:
        if collection == 'favorites':
            favorite = delete_document(favorites_collection, {'_id': _id})
            return JSONResponse(status_code=200, content=favorite)
        elif collection == 'bars':
            bar = delete_document(bars_collection, {'_id': _id})
            return JSONResponse(status_code=200, content=bar)
        elif collection == 'cafes':
            cafe = delete_document(cafes_collection, {'_id': _id})
            return JSONResponse(status_code=200, content=cafe)
        elif collection == 'restaurants':
            restaurant = delete_document(restaurants_collection, {'_id': _id})
            return JSONResponse(status_code=200, content=restaurant)
    except Exception as ex:
        raise HTTPException(status_code=500, detail=ex)


# Получить все объекты из коллекции
@app.get("/v1/{collection}")
def get_all(collection: str):
    try:
        if collection == 'favorites':
            favorite = list_all(favorites_collection)
            return JSONResponse(status_code=200, content=favorite)
        elif collection == 'bars':
            bar = list_all(bars_collection)
            return JSONResponse(status_code=200, content=bar)
        elif collection == 'cafes':
            cafe = list_all(cafes_collection)
            return JSONResponse(status_code=200, content=cafe)
        elif collection == 'restaurants':
            restaurant = list_all(restaurants_collection)
            return JSONResponse(status_code=200, content=restaurant)
    except Exception as ex:
        raise HTTPException(status_code=500, detail=ex)
