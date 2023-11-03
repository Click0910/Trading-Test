import mplfinance as mpf
import yfinance as yf
from datetime import datetime, timedelta


def get_last_three_candles(ticker='EURUSD=X', interval='30m'):
    end_date = datetime.now()
    start_date = end_date - timedelta(days=60)
    data = yf.download(ticker, start=start_date, end=end_date, interval=interval)
    last_three_candles = data.tail(3)
    return last_three_candles


# Obtener las tres últimas velas
last_3_candles = get_last_three_candles()

print(last_3_candles)

# Crear el gráfico de velas
mpf.plot(last_3_candles, type='candle', title='Last Three Hourly Candles for EUR/USD',
         show_nontrading=True)
