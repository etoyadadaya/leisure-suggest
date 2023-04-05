import requests
import random

# retrieve restaurants data
restaurants_resp = requests.get('http://127.0.0.1:8000/v1/restaurants').json()
# cafes_resp = requests.get('http://127.0.0.1:8000/v1/cafes').json()
# bars_resp = requests.get('http://127.0.0.1:8000/v1/bars').json()
# favorites_resp = requests.get('http://127.0.0.1:8000/v1/favorites').json()


# get all restaurants
def get_restaurants(restaurants_resp):
    restaurants_arr = []
    for restaurant in restaurants_resp:
        obj = restaurants_resp[f"{restaurant}"]
        link = obj["link"]
        rating = obj["rating"]
        type = obj["type"]
        address = obj["address"]
        time = obj["time"]
        metro = obj["metro"]
        phone = obj["phone"]
        restaurants_arr.append(
            f"Адрес сайта: {link}\n"
            f"Рейтинг заведения: {rating}\n"
            f"Тип заведения: {type}\n"
            f"Адресс заведения: {address}\n"
            f"Время работы: {time}\n"
            f"Станция метро: {metro}\n"
            f"Номер телефона: {phone}"
        )

    return restaurants_arr


# pick restaurant manually
def pick_restaurant(number):
    restaurants = get_restaurants(restaurants_resp)
    return restaurants[number]


# pick random restaurant
def get_random_restaurant():
    random_number = random.randrange(0, 18, 2)
    restaurants = get_restaurants(restaurants_resp)
    return restaurants[random_number]
