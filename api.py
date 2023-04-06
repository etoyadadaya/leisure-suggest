from fastapi import FastAPI
from fastapi.responses import JSONResponse
from db import insert_document, find_document, update_document, delete_document
from db import restaurants_collection, bars_collection, cafes_collection, favorites_collection

app = FastAPI()


@app.get("/v1/{collection}/{item}")
def get_place(collection: str, item: str):
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


@app.post("/v1/{collection}")
def add_place(collection: str, data: dict):
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


@app.put("/v1/{collection}/{_id}")
def update_place(collection: str, _id: int, data: dict):
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


@app.delete("/v1/{collection}/{_id}")
def delete_place(collection: str, _id: int):
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
