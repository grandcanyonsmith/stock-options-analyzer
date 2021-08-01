# from iexfinance.refdata import get_symbols

# a = Stock("AAPL", token="pk_6e6bc95937fa4794a4c6bbe6a76fd6d7")
# a.get_quote()

from xbbg import blp
SPXLAST = blp.bdh(tickers='SPX INDEX',flds='PX_LAST',start_date='09-26-18 14:30:25',end_date='09-26-18 14:30:25',TimeZone='New York')
print(SPXLAST)


