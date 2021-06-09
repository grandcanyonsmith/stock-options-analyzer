from tradingview_ta import TA_Handler, Interval, Exchange
from StockInformation.stock_indicators_analysis import stock_analysis
from twilio.rest import Client
from StockInformation.support_extract import create_resistance_report, extract_stock_previous_and_current_price

account_sid = 'AC4edaa4f9768eb268b7907e9c2680d55d'
auth_token = '22cb9fa604d5051a11787b431f79201d'
client = Client(account_sid, auth_token)

client_phone_contact = ['+18016237631','+18018752975','+13852673595']
def check():
    with open("bought.txt", "r") as stock_name:
        bought=[i.strip() for line in stock_name for i in line.split(',') if i]
        print(bought)
        return bought

def add_stock(stock):
    with open("bought.txt", "a") as stock_name:
        stock_name.write("\n"+stock)

def send_text_of_json(stock):
    five_minute_recommendation = stock_analysis(stock,'1h')
    if five_minute_recommendation == 'STRONG_BUY':    
        fifteen_minute_recommendation = stock_analysis(stock,'15m')
        if fifteen_minute_recommendation == 'STRONG_BUY':
            one_hour_recommendation = stock_analysis(stock,'5m')
            if one_hour_recommendation == 'STRONG_BUY':
                one_minute_recommendation = stock_analysis(stock,'1m')
                
                current_price, previous_close = extract_stock_previous_and_current_price(stock)
                current_price = current_price.__round__(2)
                break_through_report, breakthrough_level, time_interval, resistance, next_resistance = create_resistance_report(stock, current_price=current_price, previous_close=previous_close)
                # print(next_highest_resistance)
                print(next_resistance)
                
                if breakthrough_level == 'True':
                    resistance = float(resistance)
                    current_price = float(current_price)
                    def calculate_stock_percentage_gain_today(current_price=current_price, previous_close=previous_close):
                        previous_close = float(previous_close)
                        day_gain = (((current_price/previous_close) - 1) * 100).__round__(2)
                        return day_gain
                    
                    def calculate_stock_percentage_drop_needed_for_breaking_resistance(current_price=current_price,resistance=resistance):
                        resistance = float(resistance)
                        drop_needed = ((-(resistance/current_price)+1) * 100).__round__(2)
                        print("drop needed",drop_needed)
                        return drop_needed

                    def calculate_stock_gain_needed_to_break_next_resistance(current_price=current_price,next_resistance=next_resistance):
                        next_resistance = float(next_resistance).__round__(2)
                        print(next_resistance)
                        gain_needed = ((-(current_price/next_resistance) + 1) * 100).__round__(2)
                        print("gain needed",gain_needed)
                        return gain_needed
                       
                    day_gain = calculate_stock_percentage_gain_today(current_price=current_price,previous_close=previous_close)
                    drop_needed = calculate_stock_percentage_drop_needed_for_breaking_resistance()
                    gain_needed = calculate_stock_gain_needed_to_break_next_resistance()
                    
                    bought_list = check()
                    if stock not in bought_list:
                    

                        def send_client_text(phone_number):
                            message = client.messages.create(
                                                    body=" Trade Alert: " + stock + " $" + str(current_price) + "         +" + str(day_gain) + "%" +
                                                    # body=" Trade Alert: " + "                                 " + stock +
                                                        "\n============================" +
                                                        # "\n           Price: $"  + str(current_price) + " " + "             (+" + str(day_gain) + "%)" +
                                                        # "\n" + "(" + time_interval + ")" + " Resistance: $" + str(next_resistance) + " (+" + str(gain_needed) + "%)." +
                                                        "\n" + " Resistance: $" + str(next_resistance) + "             (+" + str(gain_needed) + "%)" +
                                                        "\n" + "(" + time_interval + ")" + "Support: $" + str(resistance) + "             (-" + str(drop_needed) + "%)",
                                                        # "\n One Minute: " + one_minute_recommendation +
                                                        # "\n Five Minute: " + five_minute_recommendation +
                                                        # "\n Fifteen Minute: " + fifteen_minute_recommendation +
                                                        # "\n One Hour: " + one_hour_recommendation,
                                                    from_='+13852336341',
                                                    to=phone_number
                                                )
                        for phone_number in client_phone_contact:
                            send_client_text(phone_number)
                        add_stock(stock)
                    else:
                        print("Already sent text for ",stock)

            else:
                pass
        else:
            pass
    else:
        pass                                                  
