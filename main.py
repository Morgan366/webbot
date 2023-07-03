
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import webbrowser

API_TOKEN = '6214212846:AAGabfTeHKjh3tPaVy2nvnhR6jJuZYxtmE4'
WEB_PAGE_URL = 'file:///E:/%D0%B1%D0%BE%D1%82/%D0%BD%D0%BE%D0%B2%D1%8B%D0%B9%20%D0%B1%D0%BE%D1%82%20%D1%81%20%D0%BD%D0%BE%D0%B2%D1%8B%D0%BC%20%D1%81%D0%B0%D0%B9%D1%82%D0%BE%D0%BC/index.html'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    markup = ReplyKeyboardMarkup()
    markup.add(KeyboardButton('Открыть веб страницу'))
    await message.answer('Здравствуйте! Нажмите "Открыть веб страницу"', reply_markup=markup)


@dp.message_handler(commands=['openwebpage'])
async def open_web_page_command(message: types.Message):
    await open_web_page(message)


@dp.message_handler(lambda message: message.text == 'Открыть веб страницу')
async def open_web_page(message: types.Message):
    # Отправка сообщения с ссылкой на веб-страницу
    await message.answer(f"Пожалуйста, [нажмите здесь]({WEB_PAGE_URL}), чтобы открыть веб страницу.")

    # Открытие веб-страницы в браузере по умолчанию
    webbrowser.open(WEB_PAGE_URL)


executor.start_polling(dp)