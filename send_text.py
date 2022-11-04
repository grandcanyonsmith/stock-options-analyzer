from StockInformation.stock_indicators_analysis import stock_analysis
from twilio.rest import Client
from StockInformation.support_extract import *
import os
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv('account_sid')
auth_token = os.getenv('auth_token')

client = Client(account_sid, auth_token)
client_phone_contact = ['+18016237631']


def get_stocks_already_sent_today():
    with open("bought.txt", "r") as stock_names:
        return [stock.strip() for line in stock_names for stock in line.split(',')]


def add_stock_to_already_sent_today_list(stock):
    print(stock)
    with open("bought.txt", "a") as stock_names:
        stock_names.write("\n"+stock)

def send_client_text(**kwargs):
    print("successfully Sent", kwargs["phone_number"])
    message = kwargs["client"].messages.create(
        body=" Trade Alert: " + kwargs["stock"] + " $" + str(kwargs["current_price"]) + "       +" + str(kwargs["day_gain"]) + "%  " + kwargs["equity_type"] + " " + 
            "\n=======================" +
            "\n" + "(" + kwargs["next_time_interval"] + ")" + " Resist. : $" + str(kwargs["next_resistance"]) + "        (+" + str(kwargs["gain_needed"]) + "%)" +
            "\n" + "(" + kwargs["past_time_interval"] + ")" + "Support: $" + str(kwargs["resistance"]) + "        (-" + str(kwargs["drop_needed"]) + "%)",
        from_='+13852336341',
        to=["+18016237631"]
    
    )
    print(message)

def analyze_equities(stock, equity_type):
    try:
        one_month = stock_analysis(stock,'1M')
        if one_month == 'STRONG_BUY':
            one_week = stock_analysis(stock,'1W')
            if one_week == 'STRONG_BUY':
                one_day = stock_analysis(stock,'1d')
                if one_day == 'STRONG_BUY':
                    four_hours = stock_analysis(stock,'4h')
                    if four_hours == 'STRONG_BUY':
                        one_hour_recommendation = stock_analysis(stock,'1h')
                        if one_hour_recommendation == 'STRONG_BUY':
                            fifteen_minute_recommendation = stock_analysis(stock,'15m')
                            if fifteen_minute_recommendation == 'STRONG_BUY':
                                five_minute_recommendation = stock_analysis(stock,'5m')
                                current_price, previous_close = get_stock_open_and_close_price(stock)
                                print(f'\n{stock} (${current_price} yesterday was ${previous_close})')

                                break_through = create_resistance_report(stock, current_price, previous_close)
                                print(break_through)
                                if break_through['break_through'] == 'True':
                                    day_gain = calculate_stock_percentage_change(current_price,previous_close)
                                    drop_needed = calculate_percentage_drop_needed_to_break_resistance(break_through['current_price'],break_through['resistance'])
                                    try:
                                        gain_needed = calculate_stock_gain_needed_to_break_next_resistance(break_through['current_price'],break_through['next_resistance'])
                                    except Exception:
                                        gain_needed = 0
                                    print(gain_needed)
                                    stocks_already_sent_today = get_stocks_already_sent_today()
                                    if stock not in stocks_already_sent_today:
                                        for phone_number in client_phone_contact:
                                            send_client_text(phone_number=phone_number,stock=stock,current_price=current_price,resistance=break_through['resistance'],day_gain=day_gain,drop_needed=drop_needed,stocks_already_sent_today=stocks_already_sent_today,next_resistance=break_through['next_resistance'],past_time_interval=str(break_through['past_time_interval']),next_time_interval=str(break_through['next_time_interval']), equity_type=equity_type, client=client, one_hour_recommendation=one_hour_recommendation, gain_needed=gain_needed)
                                        add_stock_to_already_sent_today_list(stock)
                                    else:
                                        print("Already sent text for", stock)
    except Exception as e:
        print(e)
