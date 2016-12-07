from bs4 import BeautifulSoup, SoupStrainer
import requests
import re

# Global Variables
url = "https://www.nd.edu"
sublink = re.compile("^/")
site_map = {}

# Functions
def crawl(rootURL):
    source_code = requests.get(rootURL)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "lxml", parse_only=SoupStrainer("nav", {'class': 'subnav'}))
    for nextPage in soup.find_all("a", attrs={'href': re.compile(".*")}):
        if sublink.match(nextPage):
            nextPage = rootURL + nextPage

# Main
source_code = requests.get(url)
plain_text = source_code.text
soup = BeautifulSoup(plain_text, "lxml", parse_only=SoupStrainer("nav")
for link in soup.find_all("a", attrs={'href': re.compile(".*")}):
    links = []
    nextPage = link.get('href')
    if sublink.match(nextPage):
        nextPage = url + nextPage
    links.append(nextPage)

site_map[url] = links
