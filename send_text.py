from tradingview_ta import TA_Handler, Interval, Exchange
from StockInformation.stock_indicators_analysis import stock_analysis
from twilio.rest import Client
from StockInformation.support_extract import create_resistance_report, extract_stock_previous_and_current_price

account_sid = 'AC4edaa4f9768eb268b7907e9c2680d55d'
auth_token = '22cb9fa604d5051a11787b431f79201d'
client = Client(account_sid, auth_token)

client_phone_contact = ['+18016237631','+18018752975']

def send_text_of_json(stock):
    five_minute_recommendation = stock_analysis(stock,'1h')
    if five_minute_recommendation == 'STRONG_BUY':    
        fifteen_minute_recommendation = stock_analysis(stock,'15m')
        if fifteen_minute_recommendation == 'STRONG_BUY':
            one_hour_recommendation = stock_analysis(stock,'5m')
            if one_hour_recommendation == 'STRONG_BUY':
                one_minute_recommendation = stock_analysis(stock,'1m')
                
                current_price, previous_close = extract_stock_previous_and_current_price(stock)
                break_through_report, breakthrough_level = create_resistance_report(stock, current_price=current_price, previous_close=previous_close)
                if breakthrough_level == 'True':

                    def send_client_text(phone_number):
                        message = client.messages.create(
                                                body="Stock: " + stock +
                                                    "\n Break through: " + break_through_report +
                                                    "\n One Minute: " + one_minute_recommendation +
                                                    "\n Five Minute: " + five_minute_recommendation +
                                                    "\n Fifteen Minute: " + fifteen_minute_recommendation +
                                                    "\n One Hour: " + one_hour_recommendation,
                                                from_='+13852336341',
                                                to=phone_number
                                            )
                    for phone_number in client_phone_contact:
                        send_client_text(phone_number)
            else:
                pass
        else:
            pass
    else:
        pass                                                  
