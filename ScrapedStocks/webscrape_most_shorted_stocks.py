import time
from bs4 import BeautifulSoup
from requests import get
import requests
from html.parser import HTMLParser
from json import loads
from operator import itemgetter

def scrape_most_shorted_stocks():
    page = requests.get('https://www.marketwatch.com/tools/screener/short-interest')
    soup = BeautifulSoup(page.content, 'html.parser')
    scraped_most_shorted = soup.find_all('div', class_="cell__content fixed--cell")
    most_shorted_stocks = [stock.text.strip() for stock in scraped_most_shorted]
    most_shorted_stocks.pop(0)
    return most_shorted_stocks
