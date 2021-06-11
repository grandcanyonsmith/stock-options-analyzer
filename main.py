import time
from datetime import datetime

import schedule

from ScrapedStocks.scrape_iv_stocks import scrape_highest_iv_stocks
from ScrapedStocks.webscrape_most_shorted_stocks import \
    scrape_most_shorted_stocks
from send_text import analyze_equities

most_shorted_stocks = scrape_most_shorted_stocks()
iv_stocks = scrape_highest_iv_stocks()

with open("ScrapedStocks/150_motley_fool_stocks.txt", "r") as stock_name:
    stock_list = [i.strip()
                  for line in stock_name for i in line.split(',') if i]


def main():
    while True:
        for stock in iv_stocks:
            print("\n" + "\n", stock)
            analyze_equities(stock)
        for stock in stock_list:
            print("\n" + "\n", stock)
            analyze_equities(stock)
        for stock in most_shorted_stocks:
            print("\n" + "\n", stock)
            analyze_equities(stock)


task = schedule.every().day.at("13:30").do(main)

if __name__ == '__main__':
    print("Going to run everyday at 7:30 mst")
    while True:
        schedule.run_pending()
        now = datetime.now()
        if now.hour == 20 and now.minute == 1:
            schedule.cancel_job(task)
            print("Sleeping...")
        time.sleep(1)
        # main()
