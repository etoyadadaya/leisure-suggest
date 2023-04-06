import random
import requests


# Получение случайного объекта из коллекции - Restaurants
def get_random_restaurant():
    random_number = random.randrange(0, 17, 2)
    restaurants = get_all_restaurants()
    return restaurants[random_number]


# Получение всех объектов из коллекции - Restaurants
def get_all_restaurants():
    response = requests.get(f'http://127.0.0.1:8000/v1/restaurants').json()
    restaurants_arr = []
    for item in response:
        title = item["title"]
        link = item["link"]
        rating = item["rating"]
        type = item["type"]
        address = item["address"]
        time = item["time"]
        metro = item["metro"]
        phone = item["phone"]

        restaurants_arr.append(
            f"Название: {title}\n\n"
            f"Адрес сайта: {link}\n\n"
            f"Рейтинг: {rating}\n\n"
            f"Тип заведения: {type}\n\n"
            f"Адрес: {address}\n\n"
            f"Время работы: {time}\n\n"
            f"Станция метро: {metro}\n\n"
            f"Номер телефона: {phone}\n\n"
        )

    return restaurants_arr


# Получение всех объектов из коллекции - Favorites
def get_favorites_places():
    response = requests.get(f'http://127.0.0.1:8000/v1/favorites').json()
    favorites_arr = []
    for item in response:
        title = item["title"]
        link = item["link"]
        rating = item["rating"]
        type = item["type"]
        address = item["address"]
        time = item["time"]
        metro = item["metro"]
        phone = item["phone"]

        favorites_arr.append(
            f"Название: {title}\n\n"
            f"Адрес сайта: {link}\n\n"
            f"Рейтинг заведения: {rating}\n\n"
            f"Тип заведения: {type}\n\n"
            f"Адрес заведения: {address}\n\n"
            f"Время работы: {time}\n\n"
            f"Станция метро: {metro}\n\n"
            f"Номер телефона: {phone}\n\n"
        )

    return favorites_arr
