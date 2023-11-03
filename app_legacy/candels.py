import mplfinance as mpf
import yfinance as yf
from datetime import datetime, timedelta
import pandas as pd


def get_last_three_candles(ticker='EURUSD=X', interval='1m'):
    end_date = datetime.now()
    start_date = end_date - timedelta(days=7)
    data = yf.download(ticker, start=start_date, end=end_date, interval=interval)
    last_three_candles = data.tail(3)
    return last_three_candles


# Obtener las tres últimas velas
last_3_candles = get_last_three_candles()

df = last_3_candles

pd.set_option('display.max_columns', None)

print(df)

# Crear el gráfico de velas
mpf.plot(df, type='candle', title='Last Three Hourly Candles for EUR/USD', volume=True,
         show_nontrading=True)
