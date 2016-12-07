from bs4 import BeautifulSoup, SoupStrainer
import warnings
import requests
import re

# Global Variables
fulllink = re.compile("^https://")
sublink = re.compile("^/")
allelse = re.compile("#.*")
ndDomain = re.compile(".*nd\.edu.*")

# Functions
def trade_spider(max_pages):
    page = 1
    with warnings.catch_warnings():
        while page <= max_pages:
            url = "https://www.nd.edu"
            try:
                source_code = requests.get(url)
            except:
                continue
            plain_text = source_code.text
            soup = BeautifulSoup(plain_text, "lxml")
            for link in soup.find_all('a', attrs={'href': re.compile(".*")}):
                if sublink.match(link.get('href')):
                    href = url + link.get('href')
                elif fulllink.match(link.get('href')):
                    href = link.get('href')
                else:
                    continue
                if not ndDomain.match(href):
                    continue
                
                title = link.string
                links = get_single_item_data(href)
                print href
                for l in links:
                    print l[0],
                print '\n'
            page += 1

def get_single_item_data(item_url):
    links = []
    
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "lxml")
#    for item_name in soup.find_all('nav', {'class': 'navigation'}):
#        print(item_name.string)
    for link in soup.find_all('a', attrs={'href': re.compile(".*")}):
        if sublink.match(link.get('href')):
            href = "https://nd.edu" + link.get('href')
        elif allelse.match(link.get('href')):
            continue
        else:
            href = link.get('href')
        if not ndDomain.match(href):
            continue
        title = link.string
        links.append((href, title))

    return links

# Main
trade_spider(1)
