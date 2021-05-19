import yfinance as yf
import csv

#creating a variable crypto and pointing the list of top 50 crypto by market cap to it
crypto = csv.reader(open('tickers.csv'))

for project in crypto:
    print(project)

# #pulling the compiled csv list into a tuple
    symbol, name = project
# #creating individual files for each project
    history_filename = 'history/{}.csv'.format(symbol)
# #open the file for writing
    f = open(history_filename, 'w')
# #using yfinance to screen the selected list
    ticker = yf.Ticker(symbol)
# #creating dataframe consisting of 1yr period
    df = ticker.history(period="1y")
# #writing to the csv file and creating the history
    f.write(df.to_csv())
# #close the file
    f.close()
