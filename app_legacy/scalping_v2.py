import schedule
import time
from datetime import datetime
from tradingview_ta import TA_Handler, Interval, Exchange
import json


def save_dic(dic):
    with open('tech_analysis.txt', 'a') as f:  # 'a' indica el modo append, para añadir al final del archivo
        f.write(json.dumps(dic) + '\n')  # Convertimos el diccionario a JSON y añadimos una nueva línea al final


def get_tech_analysis(option):
    while True:  # Este bucle seguirá intentando hasta que el código se ejecute con éxito
        try:

            analysis = []

            intervals = [Interval.INTERVAL_1_MINUTE, Interval.INTERVAL_5_MINUTES, Interval.INTERVAL_15_MINUTES]
            for i in range(0, len(intervals)):
                usd_eur = TA_Handler(
                    symbol=option,
                    screener="forex",
                    exchange="FX_IDC",
                    interval=intervals[i]
                )

                tech_analysis = usd_eur.get_analysis().summary
                indicators = usd_eur.get_indicators()
                tech_analysis["indicators"] = indicators
                tech_analysis["success"] = "no data"
                current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                tech_analysis["timestamp"] = current_datetime
                analysis.append(tech_analysis)
                print(tech_analysis)

            if (analysis[0]["RECOMMENDATION"] == "SELL" or analysis[0]["RECOMMENDATION"] == "STRONG SELL") \
                    and (analysis[1]["RECOMMENDATION"] == "SELL" or analysis[1]["RECOMMENDATION"] == "STRONG SELL") \
                    and (analysis[2]["RECOMMENDATION"] == "SELL" or analysis[2]["RECOMMENDATION"] == "STRONG SELL"):
                save_dic(tech_analysis)
                return "SELL"
            elif (analysis[0]["RECOMMENDATION"] == "BUY" or analysis[0]["RECOMMENDATION"] == "STRONG BUY") \
                    and (analysis[1]["RECOMMENDATION"] == "BUY" or analysis[1]["RECOMMENDATION"] == "STRONG BUY") \
                    and (analysis[2]["RECOMMENDATION"] == "BUY" or analysis[2]["RECOMMENDATION"] == "STRONG BUY"):
                save_dic(tech_analysis)
                return "BUY"

            # else:
            #     continue

            break  # Si todo se ejecutó con éxito, salir del bucle
        except Exception as e:
            print(f"Error: {e}. Reintentando en 20 segundos...")
            time.sleep(20)  # Esperar 20 segundos antes de reintentar



# Programar la ejecución de get_tech_analysis cada 1 minuto
schedule.every(1).minutes.do(lambda: get_tech_analysis("EURUSD"))

# Mantener el programa en ejecución para que la programación funcione
while True:
    schedule.run_pending()
    time.sleep(1)

