import requests
import json

finnhub_api_key_1 = 'c30dh2iad3i9gms5oiq0'
finnhub_api_key_2 = 'c1n20v237fkvp2lsh1ag'

def extract_stock_previous_and_current_price(ticker):
    r = requests.get('https://finnhub.io/api/v1/quote?symbol=' + ticker + '&token=' + finnhub_api_key_1)
    today_price_quote = r.json()    
    current_price = today_price_quote['c']
    previous_day_price = today_price_quote['pc']
    print("pc",previous_day_price)
    [print("c",current_price)]
    return current_price, previous_day_price

def get_resistance_levels(ticker, interval):
    r = requests.get('https://finnhub.io/api/v1/scan/support-resistance?symbol='+ str(ticker) + '&resolution=' + str(interval) + '&token=' + finnhub_api_key_2)
    resistance_levels = r.json()
    resistance_levels = resistance_levels['levels']
    print(resistance_levels)
    return resistance_levels

def check_if_resistance_broken(ticker, interval, current_price, previous_close):
    try:
        resistance_levels = get_resistance_levels(ticker,interval)
        for level in resistance_levels:
            level = float(level).__round__(3)
            if current_price < level:
                json = {"break_through": "False","price":current_price,"next_highest_resistance":level,"time_interval":interval}
                print(json)
                break
            else:
                if previous_close > level:
                    json = {"break_through": "False","price":current_price,"Resistance": "No Resistance Exists","time_interval":interval}
                    print(json)
                    continue
                else:
                    json = {"break_through": "True","price":current_price,"Resistance":level,"time_interval":interval}
                    print(json)
                    break
        return json
    except:
        Exception
        json = {"break_through": "No Resistance Found for this level"}
        return json

def get_all_resistance_levels(ticker,current_price,previous_close):
    resistance_level_bank = []
    resistance_levels = ['5','15','30','60','D','W']
    for level in resistance_levels:
        resistance_level_bank.append(check_if_resistance_broken(ticker,level,current_price,previous_close))

    for resistance_level in resistance_level_bank:
        if resistance_level['break_through'] == 'True':
            return resistance_level

def create_resistance_report(ticker,current_price,previous_close):
    get_resistance = get_all_resistance_levels(ticker,current_price,previous_close)
    try:
        resistance = get_resistance['Resistance']
        break_through = get_resistance['break_through']
        time_interval = get_resistance['time_interval']
        price = get_resistance['price']
        words = " crossed resistance today at " + str(resistance) + " for " + time_interval + " time interval. Price is " + str(price) + "."
        return words, break_through

    except:
        Exception
        break_through = " "
        words = "No resistance broken"
        return words, break_through