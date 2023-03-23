import pandas_datareader as pdr
# from pandas import datareader as pdr
import datetime

stock = input("Enter the stock symbol: ")
start = datetime.datetime.now() - datetime.timedelta(days=200)
end = datetime.datetime.now()

data = pdr.get_data_yahoo(stock, start=start, end=end)
average = data['Close'].mean()
minimum = data['Close'].min()
maximum = data['Close'].max()

print("200-day average: ", average)
print("200-day minimum: ", minimum)
print("200-day maximum: ", maximum)
