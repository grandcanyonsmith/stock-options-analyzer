from ScrapedStocks.scrape_iv_stocks import scrape_highest_iv_stocks
from ScrapedStocks.webscrape_most_shorted_stocks import scrape_most_shorted_stocks
from send_text import analyze_equities

most_shorted_stocks = scrape_most_shorted_stocks()
iv_stocks = scrape_highest_iv_stocks()

with open("ScrapedStocks/150_motley_fool_stocks.txt", "r") as stock_name:
    stock_list = [i.strip() for line in stock_name for i in line.split(",") if i]


def main(iv_stocks, stock_list, most_shorted_stocks):
    for stock_list, equity_type in zip([iv_stocks, stock_list, most_shorted_stocks], ["Highest IV", "Motley Fool", "Most Shorted"]):
        for stock in stock_list:
            
            print(f"\n{stock}\n{equity_type}")
            analyze_equities(stock, equity_type)


if __name__ == "__main__":
    while True:
        main(iv_stocks, stock_list, most_shorted_stocks)