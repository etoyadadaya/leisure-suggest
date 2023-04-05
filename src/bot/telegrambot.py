import os
import dotenv
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import markups as navigation
from src.main import get_restaurants
from src.main import get_random_restaurant

dotenv.load_dotenv()
token = os.getenv('TELEGRAM_TOKEN')

bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Ну что, приступим?', reply_markup=navigation.main_menu)


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Список команд', reply_markup=navigation.help_commands_menu)


@dp.message_handler()
async def bot_message(message: types.Message):
    if message.text == "Сходить покушать":
        await bot.send_message(message.from_user.id, 'Сходить покушать', reply_markup=navigation.all_tasks_menu)

    elif message.text == 'Выбрать случайно':
        restaurant = get_random_restaurant()
        await bot.send_message(message.from_user.id, restaurant)

    elif message.text == 'Выбрать ручками':
        if message.text == "0":
            restaurant = get_restaurants(0)
            await bot.send_message(message.from_user.id, restaurant)
        elif message.text == "1":
            restaurant = get_restaurants(1)
            await bot.send_message(message.from_user.id, restaurant)

    elif message.text == 'Любимые места':
        await bot.send_message(message.from_user.id, "Любимые места")

    elif message.text == 'Список команд':
        await bot.send_message(message.from_user.id, "Список команд")

    elif message.text == 'Описание команды':
        await bot.send_message(message.from_user.id, "Описание команды")

    elif message.text == 'В главное меню':
        await bot.send_message(message.from_user.id, 'Главное меню!', reply_markup=navigation.main_menu)

    else:
        await bot.send_message(message.from_user.id, "Неизвестная команда!\nВведите команду: /help, чтобы узнать о доступных командах")


if __name__ == '__main__':
    print('Running!')
    executor.start_polling(dp, skip_updates=True)
