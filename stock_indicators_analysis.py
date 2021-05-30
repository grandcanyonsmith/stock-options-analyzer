from tradingview_ta import TA_Handler, Interval, Exchange
from exchange_lookup import *

#Gets an overall analysis based off of top 20 indicators for purchasing a stock for any given time frame
# and returns a single recommendation for that time period.

def stock_analysis(stock,time_interval):
    try:
        stock_exchange = 'NASDAQ'
        handler = TA_Handler(
            symbol= stock,
            exchange=stock_exchange,
            screener="america",
            interval=time_interval,
            timeout=None
        )

        analysis = handler.get_analysis()
        summary = analysis.summary
        print(stock_exchange)
        print(summary)
        overall_recommendation = summary['RECOMMENDATION']
        return overall_recommendation

    except:
        Exception
        # print(stock, " analysis error")
        stock_analysis = nyse(stock,time_interval)
        print("NYSE",stock_analysis)
        return stock_analysis


    # else:
def nyse(stock, time_interval):
    try:
        stock_exchange = 'NYSE'
        handler = TA_Handler(
            symbol= stock,
            exchange=stock_exchange,
            screener="america",
            interval=time_interval,
            timeout=None
        )

        analysis = handler.get_analysis()
        summary = analysis.summary
        overall_recommendation = summary['RECOMMENDATION']
        return overall_recommendation
    except:
        ("NYSE ",Exception)
    

