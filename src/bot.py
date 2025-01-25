import os
import logging
import asyncio
import openai
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

# Логирование
logging.basicConfig(level=logging.INFO)

# Читаем токен из переменных окружения
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
if not TELEGRAM_TOKEN:
    raise ValueError("❌ Ошибка: переменная окружения TELEGRAM_TOKEN не установлена!")

# Создаём бота и диспетчер
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("Привет! Я бот.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
