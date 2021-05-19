#using csv to store the gathered data
import csv

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

#open the stored dataset in the csv and create a variable candles
with open('btc.csv') as f:
    reader = csv.DictReader(f)
    candles = list(reader)

#iterate through candles and print the dataset
for i in range(1, len(candles)):
    #print(candles[i])

    if is_bullish_engulfing(candles, i):
        print(" {} Bullish Engulfing".format(candles[i]["Date"]))
