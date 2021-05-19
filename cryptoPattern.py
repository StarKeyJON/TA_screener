#using csv to store the gathered data
import csv

#creating a function to test for bullish engulfing pattern
def is_bullish_candlestick(candle):
    return float(candle['Close']) > float(candle['Open'])

#creating a function to test for bearish engulfing pattern
def is_bearish_candlestick(candle):
    return float(candle['Close']) < float(candle['Open'])

#creating a new function to test for a bullish engulfing pattern
def is_bullish_engulfing(candles, index):
    current_day = candles[index]
    previous_day = candles[index-1]

    if is_bearish_candlestick(previous_day) \
        and float(current_day['Close']) > float(previous_day['Open']) \
        and float(current_day['Open']) < float(previous_day['Close']):
        return True
    
    return False

#creating a new function to test for a bearish engulfing pattern
def is_bearish_engulfing(candles, index):
    current_day = candles[index]
    previous_day = candles[index-1]

    if is_bullish_candlestick(previous_day) \
        and current_day['Open'] > previous_day['Close'] \
        and current_day['Close'] < previous_day['Open']:
        return True
    
    return False
    

#open the cryptoTickers csv file, instantiate as variable
cryptoFile = open('tickers.csv')

#read csv file
cryptoFile = csv.reader(cryptoFile)

#iterate over the file list
for project in cryptoFile:
   # print(project)

    ticker, project_name = project

    history_file = open('history/{}.csv'.format(ticker))

    reader = csv.DictReader(history_file)
    candles = list(reader)

    candles = candles[-10:]

    if len(candles) > 1:
        if is_bullish_engulfing(candles, 1):
            print("{} - {} is bullish engulfing".format(ticker, candles[1]['Date']))
