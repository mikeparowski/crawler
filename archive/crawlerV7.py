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
    with warnings.catch_warnings(): # for jobs.nd.edu 
        url = "https://www.nd.edu" # base url
        visited = set()
        while page < max_pages:
            i = 1
            if url in visited: # do not scan pages already visited
                continue 
            try:
                source_code = requests.get(url) # get socket connection object
            except:
                continue
            plain_text = source_code.text # convert object to plain text for parsing
            soup = BeautifulSoup(plain_text, "lxml") # beautifulsoup object
            for link in soup.find_all('a', attrs={'href': re.compile(".*")}): # find all links in soup
                if sublink.match(link.get('href')): # /about/asoaiwer, etc.
                    href = url + link.get('href') # connect to base url
                elif https_www.match(link.get('href')): # full url
                    href = link.get('href')
                else:
                    continue
                if not ndDomain.match(href): # don't follow links outside nd domain
                    continue
                if link.get('href').endswith('.php') or link.get('href').endswith('.pdf'): # don't follow php or pdf docs
                    continue
                
                title = link.string # get title
                links = crawl(href) # links = list of links on this page
                unique_links = set(links) # uniqify
                length = len(links)
                print href[12:-1] # slice out https://www. and final /
                # print every link associated with url
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
                        print t.replace(" ", ""), # print title 
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
