import requests
from urllib.parse import unquote

highest_iv_stocks = []

def scrape_highest_iv_stocks():
    session = requests.Session()
    main_page_url = 'https://www.barchart.com/options/highest-implied-volatility/highest?sector=stock'
    url = "https://www.barchart.com/proxies/core-api/v1/options/get?fields=symbol,baseSymbol,baseLastPrice,baseSymbolType,symbolType,strikePrice,expirationDate,daysToExpiration,bidPrice,midpoint,askPrice,lastPrice,volume,openInterest,volumeOpenInterestRatio,volatility,tradeTime,symbolCode,hasOptions&orderBy=volatility&baseSymbolTypes=stock&between(lastPrice,.10,)=&between(daysToExpiration,15,)=&between(tradeTime,2021-06-10,2021-06-11)=&orderDir=desc&between(volatility,60,)=&limit=200&between(volume,500,)=&between(openInterest,100,)=&in(exchange,(AMEX,NASDAQ,NYSE))=&meta=field.shortName,field.type,field.description&hasOptions=true&raw=1"
    payload={}
    headers = {
    'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
    'Accept': 'application/json',
    'DNT': '1',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty'
    }

    r = session.get(main_page_url,headers=headers)
    headers['X-XSRF-TOKEN'] = unquote(unquote(session.cookies.get_dict()['XSRF-TOKEN']))
    response = session.request("GET", url, headers=headers, data=payload)
    data = response.json()
    dataFrame = data['data']
    for stock_quote in dataFrame:
        stock_ticker = stock_quote['baseSymbol']
        if stock_ticker not in highest_iv_stocks:
            highest_iv_stocks.append(stock_ticker)
    print(highest_iv_stocks)
    return highest_iv_stocks




scrape_highest_iv_stocks()