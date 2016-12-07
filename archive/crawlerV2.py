from bs4 import BeautifulSoup, SoupStrainer
import requests
import warnings
import ssl
import re

# Global Variables

url = "https://www.nd.edu"
visited = set()
network_map = {}
sublink = re.compile("^/")
fulllink = re.compile("^https://")
all_links = []

# Functions

def get_links(soup):
    all_links = []
    for link in soup.find_all("a", attrs={'href': re.compile(".*")}):
        all_links.append(link.get('href'))
    return all_links

# Main
visited.add(url)
print url
source_code = requests.get(url)
plain_text = source_code.text
soup = BeautifulSoup(plain_text, "lxml", parse_only=SoupStrainer('nav'))
links = []
for link in soup.find_all("a", attrs={'href': re.compile(".*")}):
    val = link.get('href')
    if sublink.match(val):
        val = url + val
    links.append(val)

network_map[url] = links
size = len(network_map)
with warnings.catch_warnings():
    for link in links:
        if link in visited:
            continue
        warnings.simplefilter("ignore")
        try:
            source_code = requests.get(link)
        except:
            continue
        visited.add(link)
#        print link
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "lxml", parse_only=SoupStrainer('nav'))
        new_links = get_links(soup)
        network_map[link] = new_links

print "-------------------DICT----------------------"

for k in network_map:
    print k
#all_links = get_links(url, master)
#master = all_links
#for link in master:
#    master = master + all_links
#    if sublink.match(link):
#        link = url + link
#    if link not in visited:
#        all_links = get_links(link, master)
