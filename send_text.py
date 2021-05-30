from tradingview_ta import TA_Handler, Interval, Exchange
# from stock_indicators_analysis import get_input_five_minute_interval, get_input_fifteen_minute_interval, get_input_one_minute_interval, get_input_one_hour_interval, stock_analysis
from stock_indicators_analysis import stock_analysis
from twilio.rest import Client
from support_extract import create_resistance_report, extract_stock_previous_and_current_price

account_sid = 'AC4edaa4f9768eb268b7907e9c2680d55d'
auth_token = '22cb9fa604d5051a11787b431f79201d'
client = Client(account_sid, auth_token)

def send_text_of_json(stock):
    one_hour_recommendation = stock_analysis(stock,'5m')
    if one_hour_recommendation == 'STRONG_BUY':    
        fifteen_minute_recommendation = stock_analysis(stock,'15m')        
        if fifteen_minute_recommendation == 'STRONG_BUY':
            five_minute_recommendation = stock_analysis(stock,'5m')
            if five_minute_recommendation == 'STRONG_BUY':
                one_minute_recommendation = stock_analysis(stock,'1m')
                current_price, previous_close = extract_stock_previous_and_current_price(stock)
                break_through_report, breakthrough_level = create_resistance_report(stock, current_price=current_price, previous_close=previous_close)
                if breakthrough_level == 'True':


                    def send_client_text():
                        client_phone_contact = ['+18016237631']
                        for phone_number in client_phone_contact:
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
                    send_client_text()
                    # if five_minute_recommendation == 'STRONG_BUY' and fifteen_minute_recommendation == 'STRONG_BUY' or one_hour_recommendation == 'STRONG_BUY' and fifteen_minute_recommendation == 'STRONG_BUY':
                    #     send_client_text()

                    # if five_minute_recommendation == 'STRONG_BUY' and fifteen_minute_recommendation == 'STRONG_BUY' and breakthrough_level == 'True':
                    #     send_client_text()

                    # if one_minute_recommendation == 'STRONG_BUY' and fifteen_minute_recommendation == 'STRONG_BUY' and breakthrough_level == 'True':
                    #     send_client_text()

                    # if one_minute_recommendation == 'STRONG_BUY' and five_minute_recommendation == 'STRONG_BUY' and breakthrough_level == 'True':
                    #     send_client_text()
            else:
                pass
        else:
            pass
    else:
        pass                                                  
