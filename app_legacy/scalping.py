import schedule
import time
from datetime import datetime
from tradingview_ta import TA_Handler, Interval, Exchange
import json


def save_dic(dic):
    with open('tech_analysis.txt', 'a') as f:  # 'a' indica el modo append, para añadir al final del archivo
        f.write(json.dumps(dic) + '\n')  # Convertimos el diccionario a JSON y añadimos una nueva línea al final


def get_tech_analysis():
    while True:  # Este bucle seguirá intentando hasta que el código se ejecute con éxito
        try:
            usd_eur = TA_Handler(
                symbol="EURUSD",
                screener="forex",
                exchange="FX_IDC",
                interval=Interval.INTERVAL_5_MINUTES
            )

            tech_analysis = usd_eur.get_analysis().summary
            indicators = usd_eur.get_indicators()

            tech_analysis["indicators"] = indicators
            tech_analysis["success"] = "no data"

            current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            tech_analysis["timestamp"] = current_datetime

            save_dic(tech_analysis)

            print(tech_analysis)
            break  # Si todo se ejecutó con éxito, salir del bucle
        except Exception as e:
            print(f"Error: {e}. Reintentando en 20 segundos...")
            time.sleep(20)  # Esperar 20 segundos antes de reintentar

# Programar la ejecución de get_tech_analysis cada 1 minuto
schedule.every(1).minutes.do(get_tech_analysis)

# Mantener el programa en ejecución para que la programación funcione
while True:
    schedule.run_pending()
    time.sleep(1)

