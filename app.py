from send_text import send_text_of_json
import time
from scrape_shorted_stocks import scrape_most_shorted_stocks

# tickers = ['CRON']
# print("Initializing")
most_shorted_stocks = scrape_most_shorted_stocks()

with open("150_stocks.txt", "r") as stock_name:
    stock_list=[i.strip() for line in stock_name for i in line.split(',') if i]  
print(stock_list)

with open("iv_stocks.txt", "r") as stock_name:
    iv_stocks=[i.strip() for line in stock_name for i in line.split(',') if i]  
print(iv_stocks)
# @profile
def app():
    while True:
        for stock in stock_list:
        # for stock in most_shorted_stocks:
            print(stock)
            send_text_of_json(stock)
            # time.sleep(2.1)
        for stock in most_shorted_stocks:
            print(stock)
            send_text_of_json(stock)
        for stock in iv_stocks:
            print(stock)
            send_text_of_json(stock)

if __name__ == '__main__':
    app()