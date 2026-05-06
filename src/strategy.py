def check_signals(df):
    current = df.iloc[-1]
    previous = df.iloc[-2]
    
    # PRE-SIGNAL (Warning) - Used to prevent loss by alerting on partial setup
    is_pre_sell = (current['close'] < current['sma_100'] and current['rsi_9'] < 55)
    is_pre_buy = (current['close'] > current['sma_100'] and current['rsi_9'] > 45)

    # ACTUAL SELL SIGNAL [00:05:22 - 00:06:10]
    # 1. Price below SMA 100
    # 2. SuperTrend turns Red (-1)
    # 3. RSI below 50
    # 4. ZigZag confirms downward mounting
    sell_signal = (
        current['close'] < current['sma_100'] and
        current['st_direction'] == -1 and
        current['rsi_9'] < 50
    )

    # ACTUAL BUY SIGNAL (Inverse of Sell)
    buy_signal = (
        current['close'] > current['sma_100'] and
        current['st_direction'] == 1 and
        current['rsi_9'] > 50
    )

    if sell_signal: return "🔥 FINAL SELL SIGNAL (3 MIN) 🔥"
    if buy_signal: return "🚀 FINAL BUY SIGNAL (3 MIN) 🚀"
    if is_pre_sell: return "⚠️ PRE-SIGNAL: Prepare to SELL (Waiting for SuperTrend)"
    if is_pre_buy: return "⚠️ PRE-SIGNAL: Prepare to BUY (Waiting for SuperTrend)"
    
    return None
