import requests
from urllib.parse import unquote
from datetime import datetime, timedelta

def scrape_highest_iv_stocks():
    """
    Scrape the highest IV stocks from Barchart.com

    Returns:
        list: A list of stock tickers
    """
    today_date, week_ago_date = get_time()
    main_page_url = 'https://www.barchart.com/options/highest-implied-volatility/highest?sector=stock'
    url = f"https://www.barchart.com/proxies/core-api/v1/options/get?fields=symbol,baseSymbol,baseLastPrice,baseSymbolType,symbolType,strikePrice,expirationDate,daysToExpiration,bidPrice,midpoint,askPrice,lastPrice,volume,openInterest,volumeOpenInterestRatio,volatility,tradeTime,symbolCode,hasOptions&orderBy=volatility&baseSymbolTypes=stock&between(lastPrice,.10,)=&between(daysToExpiration,15,)=&between(tradeTime,{week_ago_date},{today_date})=&orderDir=desc&between(volatility,60,)=&limit=200&between(volume,500,)=&between(openInterest,100,)=&in(exchange,(AMEX,NASDAQ,NYSE))=&meta=field.shortName,field.type,field.description&hasOptions=true&raw=1"

    payload = {}
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

    with requests.Session() as session:
        r = session.get(main_page_url, headers=headers)
        headers['X-XSRF-TOKEN'] = unquote(
            unquote(session.cookies.get_dict()['XSRF-TOKEN']))
        response = session.request(
            "GET", url, headers=headers, data=payload)
        return [stock_ticker['baseSymbol'] for stock_ticker in response.json()['data']]



def get_time():
    today_date = datetime.now().strftime("%Y-%m-%d")
    week_ago_date = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
    return today_date, week_ago_date


if __name__ == "__main__":
    scrape_highest_iv_stocks()


