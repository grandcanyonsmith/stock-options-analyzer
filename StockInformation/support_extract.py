import requests
import json

finnhub_api_key_1 = 'c30dh2iad3i9gms5oiq0'
finnhub_api_key_2 = 'c1n20v237fkvp2lsh1ag'

all_resistances = []
all_levels = []

def extract_stock_previous_and_current_price(ticker):
    r = requests.get('https://finnhub.io/api/v1/quote?symbol=' + ticker + '&token=' + finnhub_api_key_1)
    today_price_quote = r.json()    
    current_price = float(today_price_quote['c']).__round__(2)
    previous_close = float(today_price_quote['pc']).__round__(2)
    return current_price, previous_close

def get_resistance_levels(ticker, interval):
    r = requests.get('https://finnhub.io/api/v1/scan/support-resistance?symbol='+ str(ticker) + '&resolution=' + str(interval) + '&token=' + finnhub_api_key_2)
    resistance_levels = r.json()
    resistance_levels = resistance_levels['levels']
    if len(resistance_levels) != 0:
        print(interval,resistance_levels)
        for x in resistance_levels:
            all_levels.append(interval)
            all_resistances.append(x)
    
    return resistance_levels

def check_if_resistance_broken(ticker, interval, current_price, previous_close):
    try:
        resistance_levels = get_resistance_levels(ticker,interval)
        i = 0
        for level in resistance_levels:
            level = float(level).__round__(2)
            i += 1
            next_highest_resistance = float(resistance_levels[i]).__round__(2)
            if current_price < level:
                json = {"break_through": "False","price":current_price,"next_highest_resistance":level,"time_interval":interval,"next_highest_resistance":next_highest_resistance}
                break
            else:
                if previous_close > level:
                    json = {"break_through": "False","price":current_price,"Resistance": "No Resistance Exists","time_interval":interval,"next_highest_resistance":next_highest_resistance}
                    continue
                else:
                    if resistance_levels[i] > current_price:
                        json = {"break_through": "True","price":current_price,"Resistance":level,"time_interval":interval,"next_highest_resistance": next_highest_resistance}
                        print("next highest",next_highest_resistance)
                        print("pc",previous_close)
                        print("c",current_price)
                        print(json)
                        break
                    else:
                        next_highest_resistance = float(resistance_levels[i+1]).__round__(2)
                        support = float(resistance_levels[i]).__round__(2)
                        json = {"break_through": "True","price":current_price,"Resistance":support,"time_interval":interval,"next_highest_resistance": next_highest_resistance}
                        print("next highest",next_highest_resistance)
                        print("pc",previous_close)
                        print("c",current_price)
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

def get_next_high_for_any_interval(current_price):
    i = 0    
    all_resistances.sort(reverse=False)
    for resistance in all_resistances:
        i += 1
        if resistance < current_price:
            continue
        else:
            return resistance, i
            break

def create_resistance_report(ticker,current_price,previous_close):
    get_resistance = get_all_resistance_levels(ticker,current_price,previous_close)
    next_highest_resistance, i = get_next_high_for_any_interval(current_price)
    # interval_for_next_highest = all_levels[i]
    # print(interval_for_next_highest)
    try:
        resistance = float(get_resistance['Resistance']).__round__(2)
        break_through = get_resistance['break_through']
        past_time_interval = get_resistance['time_interval']
        next_time_interval = all_levels[i]
        price = get_resistance['price']
        next_resistance = float(next_highest_resistance).__round__(2)
        words = " crossed resistance today at " + str(resistance) + " for " + past_time_interval + " time interval. Price is " + str(price) + "."
        return words, break_through, past_time_interval, next_time_interval, resistance, next_resistance

    except:
        Exception
        break_through = " "
        words = "No resistance broken"
        past_time_interval = " "
        next_time_interval = " "
        resistance = " "
        next_resistance = " "
        print(Exception)
        return words, break_through, past_time_interval, next_time_interval, resistance, next_resistance

def calculate_stock_percentage_gain_today(current_price, previous_close):
    previous_close = float(previous_close)
    day_gain = (((current_price/previous_close) - 1) * 100).__round__(2)
    return day_gain

def calculate_stock_percentage_drop_needed_for_breaking_resistance(current_price,resistance):
    drop_needed = ((-(resistance/current_price)+1) * 100).__round__(2)
    return drop_needed

def calculate_stock_gain_needed_to_break_next_resistance(current_price,next_resistance):
    next_resistance = float(next_resistance).__round__(2)
    gain_needed = ((-(current_price/next_resistance) + 1) * 100).__round__(2)
    return gain_needed

