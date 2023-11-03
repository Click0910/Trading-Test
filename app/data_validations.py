from tradingview_ta import TA_Handler, Interval, Exchange


def validate_data(option, interval):
    validation = TA_Handler(
        symbol=option,
        screener="forex",
        exchange="FX_IDC",
        interval=interval
    )

    return validation.get_analysis().summary
