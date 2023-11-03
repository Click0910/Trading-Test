import pandas_datareader as pdr
import datetime

start_date = datetime.datetime(2023, 9, 1)
end_date = datetime.datetime(2023, 10, 1)

data = pdr.get_data_yahoo('EURUSD=X', start=start_date, end=end_date)

print(data)
