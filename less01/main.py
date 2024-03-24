import asyncio
from concurrent.futures import Executor
import config
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
# from aiogram.utils import executor
import logging
import random
import datetime
import requests
from keyboards import kb1, kb2
from random_cat import cat
from random_fox import fox
from weather import get_weather

#Включаем логгирование
logging.basicConfig(level=logging.INFO)

#Создаем объект бота
bot = Bot(token=config.token)

#Диспечер
dp = Dispatcher()





#Хэндлер на команду /start
@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Привет, {name}', reply_markup=kb1)


#Хэндлер на команду /stop
@dp.message(Command('stop'))
async def cmd_stop(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Пока, {name}')



#Хэндлер на команду /cat
# @dp.message(Command('cat'))
# @dp.message(Command('Кошка'))
@dp.message(F.text.lower() == 'покажи кошку')
async def cmd_cat(message: types.Message):
    name = message.chat.first_name
    img_cat = cat()
    await message.answer(f'Держи кошку, {name}')
    await message.answer_photo(photo=img_cat)
# await bot.send_photo(message.from_user.id, photo=img_fox)


#Хэндлер на команду /fox
# @dp.message(Command('fox'))
# @dp.message(Command('лиса'))
@dp.message(F.text.lower() == 'покажи лису')
async def cmd_fox(message: types.Message):
    name = message.chat.first_name
    img_fox = fox()
    await message.answer(f'Держи лису, {name}')
    await message.answer_photo(photo=img_fox)
# await bot.send_photo(message.from_user.id, photo=img_fox)


#Хэндлер на команду /Погода
@dp.message(Command('get_weather'))
@dp.message(Command('погода'))
@dp.message(F.text.lower() == 'погода')

# @dp.message_handler(lambda message: message.text == "Получить погоду")
# async def get_weather_command(message: types.Message):
#     # Здесь вы можете указать город или предложить пользователю ввести его
#     city = 'Москва'
#     weather = get_weather(city)
#     await message.reply(f"Погода в {city}: {weather}°C")

# if __name__ == '__main__':
#     Executor.start_polling(dp)


async def get_weather(message: types.Message):
    try:
        response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q=москва&lang=ru&units=metric&appid=023a6a170c4ed97ffc94ab802fe5aa16")
        data = response.json()
        city = data["name"]
        cur_temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]

        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])

        # продолжительность дня
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) -       datetime.datetime.fromtimestamp(data["sys"]["sunrise"])

    except:
        await message.reply("Проверьте название города!")


code_to_smile = {
     "Clear": "Ясно \U00002600",
     "Clouds": "Облачно \U00002601",
     "Rain": "Дождь \U00002614",
     "Drizzle": "Дождь \U00002614",
     "Thunderstorm": "Гроза \U000026A1",
     "Snow": "Снег \U0001F328",
     "Mist": "Туман \U0001F32B"
}

#     # получаем значение погоды
# weather_description = date["weather"][0]["main"]

# if weather_description in code_to_smile:
#     wd = code_to_smile[weather_description]
# else:
#     # если эмодзи для погоды нет, выводим другое сообщение
#     wd = "Посмотри в окно, я не понимаю, что там за погода..."
    


#Хендлер на сообщения
@dp.message(F.text)
async def msg_echo(message: types.Message):
    msg_user = message.text.lower()
    name = message.chat.first_name
    if 'привет' in msg_user:
        await message.answer(f'Привет-привет, {name}')
    elif 'пока' == msg_user:
        await message.answer(f'Пока-пока, {name}')
    elif 'ты кто' in msg_user:
        await message.answer_dice(emoji="🎲")
    elif 'лиса' in msg_user:
        await message.answer(f'Смотри что у меня есть, {name}', reply_markup=kb2)
    else:
        await message.answer(f'Я не знаю такого слова')

async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())