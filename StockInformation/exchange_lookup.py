import requests

def look_up_exchange(tick):
    url = f'https://financialmodelingprep.com/api/v3/search?query={tick}&limit=10&apikey=API_KEY'

    r = requests.get(url)
    return r.json()[0].get('exchangeShortName')


