#using csv to store the gathered data
import csv

#identifying bullish candle
def is_bullish_candlestick(candle):
    return candle['Close'] > candle['Open']

#creating a function to test for bearish engulfing pattern
def is_bearish_candlestick(candle):
    return candle['Close'] < candle['Open']

#creating a new function to test for a bullish engulfing pattern
def is_bullish_engulfing(candles, index):
    current_day = candles[index]
    previous_day = candles[index-1]

    if is_bearish_candlestick(previous_day) \
        and current_day['Close'] > previous_day['Open'] \
        and current_day['Open'] < previous_day['Close']:
        return True
    
    return False

#creating a new function to test for a bearish engulfing pattern
def is_bearish_engulfing(candles, index):
    current_day = candles[index]
    previous_day = candles[index-1]

    if is_bullish_candlestick(previous_day) \
        and current_day['Close'] < previous_day['Open'] \
        and current_day['Open'] > previous_day['Close']:
        return True
    
    return False
