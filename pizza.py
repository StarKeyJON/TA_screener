#This is a candlestick screener application for yfinance

#Start by importing main yfinance dependency
import yfinance as yf

#choose the chart ticker to screen
btc = yf.Ticker('BTC-USD')

#selecting the dataframe period and variable
dataframe = btc.history(period="1y")

#designating the dataframe to be stored in a csv file
print(dataframe.to_csv())