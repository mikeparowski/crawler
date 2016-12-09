from bs4 import BeautifulSoup, SoupStrainer
import warnings
import requests
import re

# Global Variables
https_www = re.compile("^https://")
http = re.compile("^http://")
www = re.compile("^www.")
sublink = re.compile("^/")
allelse = re.compile("#.*")
ndDomain = re.compile(".*nd\.edu.*")
max_depth = 1

# Functions

def crawl(item_url):
    links = []
    source_code = requests.get(url)
    plain_text = source_code.text
    plain_text = plain_text.encode('utf-8').decode('utf-8')
    soup = BeautifulSoup(plain_text, "lxml")

    for link in soup.find_all('a', attrs={'href': re.compile(".*")}):
        if sublink.match(link.get('href')):
            href = item_url + link.get('href')
        elif allelse.match(link.get('href')):
            continue
        else:
            href = link.get('href')
        if not ndDomain.match(href):
            continue
        if link.get('href').endswith('.php') or link.get('href').endswith('.pdf'):
            continue

        title = link.string
        links.append((href, title))

    return links

def crawl_r(url, depth, network_map):
    # base case
    if depth is max_depth:
        return
    network_map[url] = []
    links = crawl(url)
    set(links)
    for link in links:
        network_map[url].append(link)
        crawl_r(link[0], depth+1, network_map)
    
    
# Main
url = "https://www.nd.edu"
network_map = {}
network_map[url] = []
crawl_r(url, 0, network_map)
for k in network_map:
    print k,
    for v in network_map[k]:
        if v[1] is None or v[1] is "None":
            print v[0],
        else:
            name = v[1].encode('utf-8').decode('utf-8')
            print name.replace(" ", ""),
    print
