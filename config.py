import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# Strategy Parameters [00:00:28 - 00:01:43]
SMA_PERIOD = 100
ZIGZAG_PARAMS = {'deviation': 6, 'depth': 9, 'backstep': 3}
SUPERTREND_PARAMS = {'period': 9, 'multiplier': 2}
RSI_PERIOD = 9
CANDLE_TIMEFRAME = "1m"
TRADE_DURATION = "3m"
