import requests

def look_up_exchange(tick):
    url = 'https://financialmodelingprep.com/api/v3/search?query={}&limit=10&apikey=e49e22b0865cfeea71aa0771ddf965a1'.format(tick)
    r = requests.get(url)
    return r.json()[0].get('exchangeShortName')
