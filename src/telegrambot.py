import os
import dotenv
import markups as navigation
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from utils import get_all_restaurants, get_random_restaurant, get_favorites_places

# Инициализация переменной среды
dotenv.load_dotenv()
token = os.getenv('TELEGRAM_TOKEN')

# Инициализация бота
bot = Bot(token=token)
dp = Dispatcher(bot)


# Слушатель команды - start
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Ну что, приступим?', reply_markup=navigation.main_menu)


# Слушатель команды - help
@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Список команд', reply_markup=navigation.help_commands_menu)


# Слушатель всех сообщений
@dp.message_handler()
async def bot_message(message: types.Message):
    if message.text == "Сходить покушать":
        await bot.send_message(message.from_user.id, 'Сходить покушать', reply_markup=navigation.all_tasks_menu)

    elif message.text == 'Выбрать случайно':
        restaurant = get_random_restaurant()
        await bot.send_message(message.from_user.id, restaurant)

    elif message.text == 'Выбрать ручками':
        restaurants_arr = get_all_restaurants()

        for restaurants in restaurants_arr:
            await bot.send_message(message.from_user.id, restaurants)

    elif message.text == 'Любимые места':
        favorites_arr = get_favorites_places()

        for favorite in favorites_arr:
            await bot.send_message(message.from_user.id, favorite)

    elif message.text == 'Список команд':
        await bot.send_message(message.from_user.id, "Список команд")

    elif message.text == 'Описание команды':
        await bot.send_message(message.from_user.id, "Описание команды")

    elif message.text == 'В главное меню':
        await bot.send_message(message.from_user.id, 'Главное меню!', reply_markup=navigation.main_menu)

    else:
        await bot.send_message(message.from_user.id,
                               "Неизвестная команда!\nВведите команду: /help, чтобы узнать о доступных командах")


# Точка входа в приложение
if __name__ == '__main__':
    print('Running!')
    executor.start_polling(dp, skip_updates=True)
