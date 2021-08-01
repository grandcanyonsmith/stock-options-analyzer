from send_text import analyze_equities
from ScrapedStocks.webscrape_most_shorted_stocks import scrape_most_shorted_stocks
from ScrapedStocks.scrape_iv_stocks import scrape_highest_iv_stocks

most_shorted_stocks = scrape_most_shorted_stocks()
iv_stocks = scrape_highest_iv_stocks()

with open("ScrapedStocks/150_motley_fool_stocks.txt", "r") as stock_name:
    stock_list=[i.strip() for line in stock_name for i in line.split(',') if i]  

def main():
    while True:
        for stock in iv_stocks:
            print("\n" + "\n",stock)
            equity_type = "IV Stock"
            print(equity_type)
            analyze_equities(stock, equity_type)
        for stock in stock_list:
            print("\n" + "\n",stock)
            equity_type = "Motley Fool"
            print(equity_type)
            analyze_equities(stock, equity_type)
        for stock in most_shorted_stocks:
            print("\n" + "\n",stock)
            equity_type = "Most Shorted"
            print(equity_type)
            analyze_equities(stock, equity_type)

if __name__ == '__main__':
    main()