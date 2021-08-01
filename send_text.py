from tradingview_ta import TA_Handler, Interval, Exchange
from StockInformation.stock_indicators_analysis import stock_analysis
from twilio.rest import Client
from StockInformation.support_extract import *
from env_vars import variables

account_sid = variables['account_sid']
auth_token = variables['auth_token']
client = Client(account_sid, auth_token)
# client_phone_contact = ['+18016237631','+18018752975','+13852673595']
client_phone_contact = ['+18016237631']

def get_stocks_already_sent_today():
    with open("bought.txt", "r") as stock_name:
        bought=[i.strip() for line in stock_name for i in line.split(',') if i]
        return bought

def add_stock_to_already_sent_today_list(stock):
    with open("bought.txt", "a") as stock_name:
        stock_name.write("\n"+stock)

def send_client_text(phone_number,stock,current_price,resistance,day_gain,drop_needed,stocks_already_sent_today,gain_needed,next_resistance,past_time_interval, next_time_interval,equity_type):
    message = client.messages.create(
                            body=" Trade Alert: " + stock + " $" + str(current_price) + "       +" + str(day_gain) + "%  " +  equity_type +
                                "\n=======================" +
                                "\n" + "(" + next_time_interval + ")" + " Resist. : $" + str(next_resistance) + "        (+" + str(gain_needed) + "%)" +
                                "\n" + "(" + past_time_interval + ")" + "Support: $" + str(resistance) + "        (-" + str(drop_needed) + "%)",
                                # "\n" + equity_type,
                            from_='+13852336341',
                            to=phone_number
                        )

def analyze_equities(stock, equity_type):
    try:
        one_month = stock_analysis(stock,'1M')
        one_week = stock_analysis(stock,'1W')
        if one_month == 'STRONG_BUY' and one_week == 'STRONG_BUY':
            one_day = stock_analysis(stock,'1d')
            if one_day == 'STRONG_BUY':
                four_hours = stock_analysis(stock,'4h')
                if four_hours == 'STRONG_BUY':
                    one_hour_recommendation = stock_analysis(stock,'1h')
                    fifteen_minute_recommendation = stock_analysis(stock,'15m')
                    if one_hour_recommendation == 'STRONG_BUY' and fifteen_minute_recommendation == 'STRONG_BUY':
                        five_minute_recommendation = stock_analysis(stock,'5m')
                        one_minute_recommendation = stock_analysis(stock,'1m')
                        current_price, previous_close = extract_stock_previous_and_current_price(stock)
                        break_through_report, breakthrough_level, past_time_interval, next_time_interval, resistance, next_resistance = create_resistance_report(stock, current_price=current_price, previous_close=previous_close)
                        if breakthrough_level == 'True':
                            day_gain = calculate_stock_percentage_gain_today(current_price=current_price,previous_close=previous_close)
                            drop_needed = calculate_stock_percentage_drop_needed_for_breaking_resistance(current_price=current_price,resistance=resistance)
                            gain_needed = calculate_stock_gain_needed_to_break_next_resistance(current_price=current_price,next_resistance=next_resistance)
                            stocks_already_sent_today = get_stocks_already_sent_today()

                            if stock not in stocks_already_sent_today:
                                print("okay")
                                for phone_number in client_phone_contact:
                                    send_client_text(phone_number=phone_number,stock=stock,current_price=current_price,resistance=resistance,day_gain=day_gain,drop_needed=drop_needed,gain_needed=gain_needed,stocks_already_sent_today=stocks_already_sent_today,next_resistance=next_resistance,past_time_interval=past_time_interval,next_time_interval=next_time_interval, equity_type=equity_type)
                                add_stock_to_already_sent_today_list(stock)
                            else:
                                print("Already sent text for", stock)
    except:
        Exception

# analyze_equities('PINS','FOOL')