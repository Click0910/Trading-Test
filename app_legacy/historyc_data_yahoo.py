import yfinance as yf


def get_max_high_price():

    # Define the dates range (year-month-day)
    ticker = 'EURUSD=X'
    start_date = '2023-10-27'
    end_date = '2023-11-01'

    # Download data
    data = yf.download(ticker, start=start_date, end=end_date)
    max_high_price = data['High'].max()
    max_high_row = data['High'].idxmax()

    # show info max price
    return max_high_price, max_high_row


# def get_min_price():
#
#     # Define the dates range (year-month-day)
#     ticker = 'EURUSD=X'
#     start_date = '2023-10-27'
#     end_date = '2023-11-01'
#
#     # Download data
#     data = yf.download(ticker, start=start_date, end=end_date)
#     min_low_price = data['Low'].min()
#     min_low_row = data.loc[data['Low'].idxmin()]
#
#     # show info max price
#     return min_low_price, min_low_row


# Define the dates range (year-month-day)
ticker = 'EURUSD=X'
start_date = '2023-10-27'
end_date = '2023-11-01'

# Descargar datos
data = yf.download(ticker, start=start_date, end=end_date)

# Mostrar los primeros datos
print(data.head())

max_price, max_row = get_max_high_price()

print(max_row)


# print(get_min_price())
