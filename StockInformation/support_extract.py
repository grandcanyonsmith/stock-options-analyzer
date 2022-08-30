import requests
import os
from dotenv import load_dotenv
load_dotenv()
finnhub_api_key= os.getenv('FINNHUB_API_KEY_2')

def get_stock_open_and_close_price(ticker):
    url = 'https://finnhub.io/api/v1/quote?symbol={}&token={}'.format(ticker, finnhub_api_key)
    response = requests.get(url)
    today_price_quote = response.json()
    return round(float(today_price_quote['c']), 2), round(float(today_price_quote['pc']), 2)

    
def extract_stock_previous_and_current_price(ticker):
    current_price, previous_close = get_stock_open_and_close_price(ticker)
    return current_price, previous_close


def get_stock_resistance_levels(ticker, interval):
    url = (
        'https://finnhub.io/api/v1/scan/support-resistance'
        '?symbol={}&resolution={}&token={}'
    ).format(ticker, interval, finnhub_api_key)
    r = requests.get(url).json()
    levels = [round(level, 2) for level in r['levels']]
    return levels


def check_if_resistance_broken(ticker, interval, current_price, previous_close):
    resistance_levels = get_stock_resistance_levels(ticker, interval)

    for i, resistance in enumerate(resistance_levels):
        resistance = round(float(resistance), 2)
        if current_price > resistance and previous_close < resistance:
            # next_highest_resistance = round(float(resistance_levels[i + 1]), 2) if i != len(resistance_levels) - 1 else last resistance level
            next_highest_resistance = round(float(resistance_levels[i + 1]), 2) if i != len(resistance_levels) - 1 else resistance_levels[-1]
            print("ffff",resistance, next_highest_resistance)
            print(f"{ticker} crossed resistance today at {resistance} for {interval} time interval. Price is {current_price}.")
            print(resistance_levels[i + 1])
            print(resistance)
            print(interval)
            if i != (len(resistance_levels) - 1):
                next_interval = resistance_levels[i + 1]
                breakthrough = 'True'
                sonson = {'break_through': "True", 'resistance': resistance, 'past_time_interval': interval, 'next_resistance': next_highest_resistance, 'next_time_interval': resistance_levels[i + 1], "next_highest_resistance": next_highest_resistance} if i != (len(resistance_levels) - 1) else {'break_through': True, 'breakthrough_level': resistance, 'past_time_interval': interval, 'next_time_interval': None}
                # son = {"break_through": "True","price":current_price,"Resistance":level,"time_interval":interval,"next_highest_resistance": next_highest_resistance}
                # return {'break_through': True, 'breakthrough_level': resistance, 'past_time_interval': interval, 'next_time_interval': resistance_levels[i + 1]} if i != (len(resistance_levels) - 1) else {'break_through': True, 'breakthrough_level': resistance, 'past_time_interval': interval, 'next_time_interval': None}
                return sonson
                break
                # return breakthrough, resistance, interval, next_interval
            else:
                
                return {'breakthrough_level': None, 'resistance': resistance, 'next_resistance': next_highest_resistance, 'percentage_change': calculate_stock_percentage_change(current_price, previous_close), 'percentage_drop_needed': calculate_percentage_drop_needed_to_break_resistance(current_price, resistance), 'percentage_gain_needed': calculate_stock_gain_needed_to_break_next_resistance(current_price, next_highest_resistance), 'ticker': ticker, 'current_price': current_price, 'previous_close': previous_close, 'next_highest_resistance': next_highest_resistance}
    # return None

def get_all_resistance_levels_for_stock(ticker,current_price,previous_close):
    return [check_if_resistance_broken(ticker, interval, current_price, previous_close) for interval in ['1', '5', '15', '30', '60', 'D']]


def create_resistance_report(ticker, current_price, previous_close):
    all_resistances = [x for x in get_all_resistance_levels_for_stock(ticker, current_price, previous_close) if x]
    if not all_resistances: return {'words': None, 'break_through': None, 'past_time_interval': None, 'next_time_interval': None, 'resistance': None, 'next_resistance': None, 'percentage_change': None, 'percentage_drop_needed': None, 'percentage_gain_needed': None, 'ticker': ticker, 'current_price': current_price, 'previous_close': previous_close, 'next_highest_resistance': None}
    print('f',all_resistances)
    all_resistances = sorted(all_resistances, key=lambda i: i['resistance'])
    print('f',all_resistances)
    for i, resistance in enumerate(all_resistances):
        if resistance['break_through'] == "True":
            next_highest_resistance = round(float(all_resistances[i + 1]['resistance']), 2) if i != len(all_resistances) - 1 else None
            print("ffff",resistance, next_highest_resistance)
            break_through = "True"
            
            print("fa",break_through, resistance['resistance'], resistance['past_time_interval'], resistance['next_time_interval'], next_highest_resistance)
            return {'break_through': break_through, 'breakthrough_level': resistance['resistance'], 'past_time_interval': resistance['past_time_interval'], 'next_resistance': resistance['next_resistance'], 'next_time_interval': all_resistances[i + 1]['past_time_interval'] if i != len(all_resistances) - 1 else None, 'resistance': resistance['resistance'], 'next_resistance': next_highest_resistance, 'percentage_change': round((resistance['resistance'] - previous_close) / previous_close * 100, 2), 'percentage_drop_needed': round((resistance['resistance'] - previous_close) / previous_close * 100 - 100, 2), 'percentage_gain_needed': round(100 - (resistance['resistance'] - previous_close) / previous_close * 100, 2), 'ticker': ticker, 'current_price': current_price, 'previous_close': previous_close, 'next_highest_resistance': next_highest_resistance}

    

def calculate_stock_percentage_change(current_price, previous_close):
    return round((-(current_price - previous_close) / previous_close) * 100, 2) if previous_close else None

def calculate_percentage_drop_needed_to_break_resistance(current_price,resistance):
    return round(((-(resistance - current_price) / current_price) * 100)-100, 2)

def calculate_stock_gain_needed_to_break_next_resistance(current_price,next_resistance):
    return round(((-(next_resistance - current_price) / current_price) * 100)+100, 2) if next_resistance else None

def calculate_percentage_change_in_stock(current_price, previous_close, resistance, next_resistance):
    values = [previous_close, resistance, next_resistance]
    for i in range(len(values)):
        if values[i]:
            return round(((values[i] - current_price) / values[i]) * 100, 2)
