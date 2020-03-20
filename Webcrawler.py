import requests
from bs4 import BeautifulSoup


def trade_spider(max_pages):
    page = 0
    x = 0
    y = 0
    prices = {}
    while (page < max_pages):
        url = "https://sfbay.craigslist.org/search/sby/sop?s=" + str(page)
        source_code = requests.get(url)
        plain_text =  source_code.text
        #print(plain_text)
        soup = BeautifulSoup(plain_text,  "html.parser")
        #print(soup)
        for money in soup.findAll("span", {"class" : "result-price"}):
            prices[x] = money.string
            x += 1
        for link in soup.findAll("a", {"class" : "hdrlnk"}):
            #print(link)
            href = link.get("href")
            title = link.string
            print(prices[y])
            print(title)
            print(href)
            y += 2
            get_single_item_data(href)
        page += 1

def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for item_name in soup.findAll("section", {"id" : "postingbody"}):
        # print (item_name.text)
        print("\n\n\n\n\n\n")
    for link in soup.findAll("a", href=True):
        href = link.get("href")
        #print(href)

trade_spider(1)
