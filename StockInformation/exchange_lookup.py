import requests

def look_up_exchange(tick):
    url = f'https://financialmodelingprep.com/api/v3/search?query={tick}&limit=10&apikey=e49e22b0865cfeea71aa0771ddf965a1'

    r = requests.get(url)
    return r.json()[0].get('exchangeShortName')
