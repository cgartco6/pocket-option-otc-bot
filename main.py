import time
import pandas as pd
from src.indicators import apply_indicators
from src.strategy import check_signals
from src.telegram_bot import send_signal
import asyncio

async def run_bot():
    print("Bot is scanning Pocket Option OTC Market...")
    while True:
        # Note: In a real scenario, replace this with a WebSocket 
        # or API call to Pocket Option to get live candle data.
        raw_data = fetch_market_data() 
        df = apply_indicators(raw_data)
        
        signal = check_signals(df)
        if signal:
            await send_signal(signal)
            
        await asyncio.sleep(60) # Wait for next 1m candle

if __name__ == "__main__":
    asyncio.run(run_bot())
