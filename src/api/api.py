from fastapi import FastAPI
from data import restaurants, bars, cafes, favorites

app = FastAPI()


@app.get("/v1/restaurants")
def get_restaurants():
    return restaurants


@app.get("/v1/cafes")
def get_cafes():
    return cafes


@app.get("/v1/bars")
def get_bars():
    return bars


@app.get("/v1/favorites")
def get_favorites():
    return favorites
