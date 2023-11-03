import yfinance as yf


def get_max_min_price():
    # Define the dates range (year-month-day)
    ticker = 'EURUSD=X'
    start_date = '2023-10-26'
    end_date = '2023-11-02'

    # Download data
    data = yf.download(ticker, start=start_date, end=end_date)
    max_high_price = data['High'].max()
    max_price_date = data['High'].idxmax()
    min_low_price = data['Low'].min()
    min_price_date = data['Low'].idxmin()
    min_low_row = data.loc[data['Low'].idxmin()]
    max_high_row = data.loc[data['High'].idxmax()]

    # show info max price
    return max_high_price, max_price_date, min_low_price, min_price_date, min_low_row, max_high_row, data


a, b, c, d, e, f, g = get_max_min_price()

print(f"{a}\n"
      f"{b}\n"
      f"{c}\n"
      f"{d}\n"
      f"{e}\n"
      f"{f}\n"
      f"{g}\n"
      )
