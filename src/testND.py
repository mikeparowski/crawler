from bs4 import BeautifulSoup, SoupStrainer
import requests
import warnings
import ssl
import re

# Global Variables

url = "https://www.nd.edu"
visited = set()
sublink = re.compile("^/")
all_links = []

# Functions

def get_links(url, all_links):
    visited.add(url)
    print url
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        try:
            source_code = requests.get(url)
        except:
#            print "%s threw an SSL error" % url
            all_links.remove(url)
            return all_links
    all_links = []
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "lxml", parse_only=SoupStrainer('nav'))
    for link in soup.find_all("a", attrs={'href': re.compile(".*")}):
        all_links.append(link.get('href'))
    return all_links

# Main
dummy = []
all_links = get_links(url, dummy)
for link in all_links:
    if sublink.match(link):
        link = url + link
    if link not in visited:
        get_links(link, all_links)
