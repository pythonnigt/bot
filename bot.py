import asyncio
import logging
import os

from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    WebAppInfo
)

from aiohttp import TCPConnector
from aiohttp.resolver import AsyncResolver
from aiogram.client.session.aiohttp import AiohttpSession

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBAPP_URL = os.getenv("WEBAPP_URL")

# ===== CUSTOM DNS RESOLVER =====
resolver = AsyncResolver(
    nameservers=["8.8.8.8", "1.1.1.1"]
)

connector = TCPConnector(
    resolver=resolver,
    family=2
)

session = AiohttpSession(
    connector=connector
)

bot = Bot(
    token=BOT_TOKEN,
    session=session
)

dp = Dispatcher()


@dp.message(CommandStart())
async def start_command(message: types.Message):

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="💰 Kripto Narxlarni Ko‘rish",
                    web_app=WebAppInfo(url=WEBAPP_URL)
                )
            ]
        ]
    )

    await message.answer(
        "Assalomu alaykum! 👋\n\n"
        "Kripto bozoridagi narxlarni ko‘rish uchun tugmani bosing:",
        reply_markup=keyboard
    )


async def main():

    logging.basicConfig(level=logging.INFO)

    while True:
        try:
            print("Bot ishga tushdi...")
            await dp.start_polling(bot)

        except Exception as e:
            logging.error(f"Xatolik: {e}")

            print("5 sekunddan keyin qayta ulanadi...")
            await asyncio.sleep(5)


if __name__ == "__main__":
    asyncio.run(main()) 
# import asyncio
# import logging
# from aiogram import Bot, Dispatcher, types
# from aiogram.filters import CommandStart
# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
# from dotenv import load_dotenv
# import os

# load_dotenv()

# BOT_TOKEN = os.getenv("BOT_TOKEN")
# WEBAPP_URL = os.getenv("WEBAPP_URL")   # Vercel linkini qo‘ying

# bot = Bot(token=BOT_TOKEN)
# dp = Dispatcher()

# @dp.message(CommandStart())
# async def start_command(message: types.Message):
#     keyboard = InlineKeyboardMarkup(inline_keyboard=[
#         [InlineKeyboardButton(text="💰 Kripto Narxlarni Ko‘rish", web_app=WebAppInfo(url=WEBAPP_URL))]
#     ])
    
#     await message.answer(
#         "Assalomu alaykum! 👋\n\nKripto bozoridagi narxlarni ko‘rish uchun tugmani bosing:",
#         reply_markup=keyboard
#     )

# async def main():
#     logging.basicConfig(level=logging.INFO)
    
#     # DNS va ulanish muammolarini kamaytirish uchun
#     try:
#         await dp.start_polling(bot)
#     except Exception as e:
#         logging.error(f"Xatolik: {e}")
#         await asyncio.sleep(5)

# if __name__ == "__main__":
#     asyncio.run(main())