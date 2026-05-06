import pandas_ta as ta
import pandas as pd

def apply_indicators(df):
    # SMA 100 [00:00:28]
    df['sma_100'] = ta.sma(df['close'], length=100)
    
    # RSI 9 [00:01:34]
    df['rsi_9'] = ta.rsi(df['close'], length=9)
    
    # SuperTrend [00:01:20]
    st = ta.supertrend(df['high'], df['low'], df['close'], length=9, multiplier=2)
    df['st_direction'] = st['SUPERTd_7_2.0'] # 1 for up, -1 for down
    
    # ZigZag [00:00:52] (Custom logic often required for ZigZag in Pandas)
    # Using a simplified high/low swing logic for signal purposes
    df['zigzag'] = ta.zigzag(df['close'], deviation=6) 
    
    return df
