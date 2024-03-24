import asyncio
import config
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
import logging

bot = Bot(token=config.token)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_cmd(message: types.Message) -> None:
    name = message.chat.first_name
    await message.answer('Это была команда старт')
    
@dp.message()
async def echo(message: types.Message) -> None:
    name = message.chat.first_name
    text: str | None = message.text
    
    if text in ['Привет', 'привет', 'hi', 'hello']:
        await message.answer(f'И тебе, {name} привет!')
    elif text in ['Пока', 'пока', 'чау', 'До свидания']:
        await message.answer(f'И тебе, {name} пока!') 
    else:    
        await message.answer(message.text)
    
    
async def main() -> None:
        await dp.start_polling(bot)
        
asyncio.run(main())