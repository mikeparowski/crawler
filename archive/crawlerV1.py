from bs4 import BeautifulSoup, SoupStrainer
import requests
import warnings
import ssl
import re

# Global Variables

url = "https://www.nd.edu"
visited = set()
sublink = re.compile("^/")
fulllink = re.compile("^https://")
all_links = []
web_map = {}
# Functions

def get_links(url, all_links):
    visited.add(url)
    print url
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        try:
            source_code = requests.get(url)
        except:
            print "%s threw an SSL error" % url
            all_links.remove(url)
            return all_links
        all_links = []
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "lxml", parse_only=SoupStrainer('nav'))
        for link in soup.find_all("a", attrs={'href': re.compile(".*")}):
            all_links.append(link.get('href'))
        return all_links

# Main
master = []
all_links = get_links(url, master)
web_map[url] = all_links
for link in master:
    master = master + all_links
    if sublink.match(link):
        link = url + link
    if link not in visited:
        all_links = get_links(link, master)
