from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types.web_app_info import WebAppInfo

back_btn = KeyboardButton("В главное меню")

# -----------------------Main menu---------------------------

all_tasks_btn = KeyboardButton("Сходить покушать")
web_app_btn = KeyboardButton("Открыть страницу", web_app=WebAppInfo(url="https://ya.ru"))
main_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(all_tasks_btn, web_app_btn)

# -----------------------All tasks menu----------------------

waiting_tasks_btn = KeyboardButton("Выбрать случайно")
progress_tasks_btn = KeyboardButton("Выбрать ручками")
favorites_tasks_btn = KeyboardButton("Любимые места")
all_tasks_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(waiting_tasks_btn, progress_tasks_btn, favorites_tasks_btn, back_btn)

# -----------------------Help menu---------------------------

help_commands_btn = KeyboardButton("Список команд")
help_description_btn = KeyboardButton("Описание команды")
help_find_btn = KeyboardButton("Найти команду")
help_commands_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(help_commands_btn, help_description_btn, help_find_btn, back_btn)
