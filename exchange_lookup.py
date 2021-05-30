import requests

def look_up_exchange(tick):
    r = requests.get('https://financialmodelingprep.com/api/v3/search?query=' + tick + '&limit=10&apikey=e49e22b0865cfeea71aa0771ddf965a1')
    stock_exchange = r.json()
    stock_exchange = stock_exchange[0]['exchangeShortName']
    print(stock_exchange)
    
    return stock_exchange