from send_text import send_text_of_json
import time
from ScrapedStocks.webscrape_most_shorted_stocks import scrape_most_shorted_stocks

most_shorted_stocks = scrape_most_shorted_stocks()

with open("ScrapedStocks/150_motley_fool_stocks.txt", "r") as stock_name:
    stock_list=[i.strip() for line in stock_name for i in line.split(',') if i]  

with open("ScrapedStocks/highest_IV_stocks.txt", "r") as stock_name:
    iv_stocks=[i.strip() for line in stock_name for i in line.split(',') if i]  

def main():
    while True:
        for stock in stock_list:
            print(stock)
            send_text_of_json(stock)
        for stock in most_shorted_stocks:
            print(stock)
            send_text_of_json(stock)
        for stock in iv_stocks:
            print(stock)
            send_text_of_json(stock)

if __name__ == '__main__':
    main()