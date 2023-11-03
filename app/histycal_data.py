import yfinance as yf


def get_max_min_price():

    # Define the dates range (year-month-day)
    ticker = 'EURUSD=X'
    start_date = '2008-11-02'
    end_date = '2023-11-02'

    # Download data
    data = yf.download(ticker, start=start_date, end=end_date)
    max_high_price = data['High'].max()
    max_price_date = data['High'].idxmax()
    min_low_price = data['Low'].min()
    min_price_date = data['Low'].idxmin()

    # show info max price
    return max_high_price, max_price_date, min_low_price, min_price_date