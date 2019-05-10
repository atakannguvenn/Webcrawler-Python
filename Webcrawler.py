import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page = 0
    while (page < max_pages):
        url = "https://sfbay.craigslist.org/search/sby/sop?s=" + str(page)
        source_code = requests.get(url)
        plain_text =  source_code.text
        soup = BeautifulSoup(plain_text,  "html.parser")
        for link in soup.findAll("a", {"class" : "hdrlnk"}):
            href = "https://sfbay.craigslist.org" + link.get("href")
            title = link.string
            #print(title)
            #print(href)
            get_single_item_data(href)
        page += 100
        max_pages += 99

def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for item_name in soup.findAll("span", {"id" : "titletextonly"}):
        print (item_name.string)
    for link in soup.findAll("a", href=True):
        href = "https://sfbay.craigslist.org" + link.get("href")
        print(href)

trade_spider(1)