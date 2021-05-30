#Ways to make the aglo faster
#1. Only run the shorted stocks list once per day; it shouldn't refresh more than this time interval.
#2. First answer: "Is 15m strong buy?" If not, then exit out and more to the next ones. If it is, then get it for the rest of them.
#3. Don't run queries on finnhub, stock analysis unless all recommendation intervals are met.



#test the speed of how long it takes JUST to get if the 15 minute interval is STRONG buy for every stock in a list


from tradingview_ta import TA_Handler, Interval, Exchange
from exchange_lookup import *

#Gets an overall analysis based off of top 20 indicators for purchasing a stock for any given time frame
# and returns a single recommendation for that time period.


test_list = ['PINS','FUBO','NAKD','CRON','QRVO','AAPL','NVDA','GRUB','ABNB','TSLA']

@profile
def stock_analysis():
    for stock in test_list:
        try:
            stock_exchange = look_up_exchange(stock)
            handler = TA_Handler(
                symbol= stock,
                exchange=stock_exchange,
                screener="america",
                interval='15m',
                timeout=None
            )

            analysis = handler.get_analysis()
            summary = analysis.summary
            print(summary)
            overall_recommendation = summary['RECOMMENDATION']
            # return overall_recommendation

        except:
            Exception
            print(stock, " analysis error")
stock_analysis()
            