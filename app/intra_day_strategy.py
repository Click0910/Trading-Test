from tradingview_ta import TA_Handler, Interval, Exchange
from datetime import datetime
from app.histycal_data import get_max_min_price
from app.data_validations import validate_data


'''
symbol: EURUSD
Exchange:
Screener:

Symbol: Gold


'''


def get_analysis(option: str):
    analysis = []

    intervals = [Interval.INTERVAL_30_MINUTES, Interval.INTERVAL_1_HOUR, Interval.INTERVAL_2_HOURS]
    for i in range(0, len(intervals)):
        option_test = TA_Handler(
            symbol=option,
            screener="forex",
            exchange="FX_IDC",
            interval=intervals[i]
        )

        tech_analysis = option_test.get_analysis().summary
        indicators = option_test.get_indicators()
        tech_analysis["indicators"] = indicators
        tech_analysis["success"] = "no data"
        current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        tech_analysis["timestamp"] = current_datetime

        analysis.append(tech_analysis)

    if (analysis[0]["RECOMMENDATION"] == "SELL" or analysis[0]["RECOMMENDATION"] == "STRONG SELL") \
            and (analysis[1]["RECOMMENDATION"] == "SELL" or analysis[1]["RECOMMENDATION"] == "STRONG SELL") \
            and (analysis[2]["RECOMMENDATION"] == "SELL" or analysis[2]["RECOMMENDATION"] == "STRONG SELL"):
        for element in analysis:
            print(element)

        max_price, max_date, min_price, min_date = get_max_min_price()
        print(
            f"----------------max historical price:---------------\n"
            f"max price: {max_price}\n"
            f"{max_date}\n"
            f"-----------------min historical price---------------\n"
            f"min price: {min_price}\n"
            f"{min_date}\n"
            f"----------------------###############-----------------\n"
            f"This is the current price: {analysis[2]['indicators']['close']}"
            f"\n------------------#######---------------")

        return "This is the recommendation: SELL"
    elif (analysis[0]["RECOMMENDATION"] == "BUY" or analysis[0]["RECOMMENDATION"] == "STRONG BUY") \
            and (analysis[1]["RECOMMENDATION"] == "BUY" or analysis[1]["RECOMMENDATION"] == "STRONG BUY") \
            and (analysis[2]["RECOMMENDATION"] == "BUY" or analysis[2]["RECOMMENDATION"] == "STRONG BUY"):
        for element in analysis:
            print(element)

        max_price, max_date, min_price, min_date = get_max_min_price()
        print(
            f"----------------max historical price:---------------\n"
            f"max price: {max_price}\n"
            f"{max_date}\n"
            f"------------------min historical price---------------\n"
            f"min price: {min_price}\n"
            f"{min_date}\n"
            f"----------------------###############-----------------\n"
            f"This is the current price: {analysis[2]['indicators']['close']}"
            f"\n------------------#######---------------")

        return "This is the recommendation: BUY"

    else:
        for element in analysis:
            print(element)
        max_price, max_date, min_price, min_date = get_max_min_price()
        print(
            f"----------------max historical price:---------------\n"
            f"max price: {max_price}\n"
            f"{max_date}\n"
            f"------------------min historical price---------------\n"
            f"min price: {min_price}\n"
            f"{min_date}\n"
            f"----------------------###############-----------------\n"
            f"This is the current price: {analysis[2]['indicators']['close']}"
            f"\n------------------#######---------------")

        return "Is not moment to make any movement"


print(get_analysis("EURUSD"))


print(f"----------------############------------\n"
      f"this is the validation: {validate_data('EURUSD', Interval.INTERVAL_1_DAY)}")
