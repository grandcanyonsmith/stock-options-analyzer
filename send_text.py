from tradingview_ta import TA_Handler, Interval, Exchange
from StockInformation.stock_indicators_analysis import stock_analysis
from twilio.rest import Client
from StockInformation.support_extract import *
from env_vars import variables

account_sid = variables['account_sid']
auth_token = variables['auth_token']
client = Client(account_sid, auth_token)
# client_phone_contact = ['+18016237631']
client_phone_contact = ['+18016237631','+18018752975','+13852673595']

def get_stocks_already_sent_today():
    with open("bought.txt", "r") as stock_name:
        bought=[i.strip() for line in stock_name for i in line.split(',') if i]
        return bought

def add_stock_to_already_sent_today_list(stock):
    with open("bought.txt", "a") as stock_name:
        stock_name.write("\n"+stock)

def send_client_text(phone_number,stock,current_price,resistance,day_gain,drop_needed,stocks_already_sent_today,gain_needed,next_resistance,time_interval):
    message = client.messages.create(
                            body=" Trade Alert: " + stock + " $" + str(current_price) + "         +" + str(day_gain) + "%" +
                                "\n=======================" +
                                "\n" + " Resistance: $" + str(next_resistance) + "             (+" + str(gain_needed) + "%)" +
                                "\n" + "(" + time_interval + ")" + "Support: $" + str(resistance) + "             (-" + str(drop_needed) + "%)",
                            from_='+13852336341',
                            to=phone_number
                        )

def analyze_equities(stock):
    five_minute_recommendation = stock_analysis(stock,'5m')
    if five_minute_recommendation == 'STRONG_BUY':    
        fifteen_minute_recommendation = stock_analysis(stock,'15m')

        if fifteen_minute_recommendation == 'STRONG_BUY':
            one_hour_recommendation = stock_analysis(stock,'1h')

            if one_hour_recommendation == 'STRONG_BUY':
                one_minute_recommendation = stock_analysis(stock,'1m')
                current_price, previous_close = extract_stock_previous_and_current_price(stock)
                break_through_report, breakthrough_level, time_interval, resistance, next_resistance = create_resistance_report(stock, current_price=current_price, previous_close=previous_close)

                if breakthrough_level == 'True':
                    day_gain = calculate_stock_percentage_gain_today(current_price=current_price,previous_close=previous_close)
                    drop_needed = calculate_stock_percentage_drop_needed_for_breaking_resistance(current_price=current_price,resistance=resistance)
                    gain_needed = calculate_stock_gain_needed_to_break_next_resistance(current_price=current_price,next_resistance=next_resistance)
                    stocks_already_sent_today = get_stocks_already_sent_today()

                    if stock not in stocks_already_sent_today:
                        for phone_number in client_phone_contact:
                            send_client_text(phone_number=phone_number,stock=stock,current_price=current_price,resistance=resistance,day_gain=day_gain,drop_needed=drop_needed,gain_needed=gain_needed,stocks_already_sent_today=stocks_already_sent_today,next_resistance=next_resistance,time_interval=time_interval)
                        add_stock_to_already_sent_today_list(stock)
                    else:
                        print("Already sent text for", stock)