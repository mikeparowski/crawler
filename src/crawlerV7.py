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

# Functions
def trade_spider(max_pages):
    page = 1
    with warnings.catch_warnings():
        url = "https://www.nd.edu"
        visited = set()
        while page <= max_pages:
            i = 0
            if url in visited:
                continue 
            try:
                source_code = requests.get(url)
            except:
                continue
            plain_text = source_code.text
            soup = BeautifulSoup(plain_text, "lxml")
            for link in soup.find_all('a', attrs={'href': re.compile(".*")}):
                if sublink.match(link.get('href')):
                    href = url + link.get('href')
                elif https_www.match(link.get('href')):
                    href = link.get('href')
                else:
                    continue
                if not ndDomain.match(href):
                    continue
                if link.get('href').endswith('.php') or link.get('href').endswith('.pdf'):
                    continue
                
                title = link.string
                links = crawl(href)
                unique_links = set(links)
                length = len(links)
                print href[12:-1] # slice out https://www. and final /
                for l in unique_links:
                    if l[1] is "None" or l[1] is None: # print abbreviated url if no title 
                        abbrv = l[0]
                        abbrv.encode('utf-8').decode('utf-8')
                        if https_www.match(abbrv):
                            print abbrv[12:-1], # https://www.
                        elif http.match(abbrv):
                            print abbrv[7:-1], # http://
                        elif www.match(abbrv):
                            print abbrv[4:-1], # www.
                    else:
                        t = l[1]
                        t.encode('utf-8').decode('utf-8')
                        print t, # print title 
                print '\n'
            visited.add(url)
            if i < length:
                url = links[i]
                i += 1
            page += 1

def crawl(item_url):
    links = []
    
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "lxml")

    for link in soup.find_all('a', attrs={'href': re.compile(".*")}):
        if sublink.match(link.get('href')):
            href = "https://nd.edu" + link.get('href')
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

# Main
trade_spider(1)
