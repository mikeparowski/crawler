import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = "https://www.nd.edu/"
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "lxml")
        for link in soup.find_all('a', {'class': 'item-name'}):
            href = "https://buckysroom.org" + link.get('href')
            title = link.string
            get_single_item_data(href))
#            print(href)
#            print(title)
        page += 1

def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for item_name in soup.find_all('div', {'class': 'i-name'}):
        print(item_name.string)
    for link in soup.find_all('a'):
        href = "https://buckysroom.org" + link.get('href')

trade_spider(3)
