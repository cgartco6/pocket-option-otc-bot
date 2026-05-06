from telegram import Bot
import asyncio
from config import TELEGRAM_TOKEN, CHAT_ID

bot = Bot(token=TELEGRAM_TOKEN)

async def send_signal(message):
    await bot.send_message(chat_id=CHAT_ID, text=message)
