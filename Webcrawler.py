import requests
from bs4 import BeautifulSoup


def web_scraper(max_pages):
    page = 0
    while (page < max_pages):
        url = "https://sfbay.craigslist.org/search/sby/sop?s=" + str(page)
        source_code = requests.get(url)
        plain_text =  source_code.text
        # print(plain_text)
        soup = BeautifulSoup(plain_text,  "html.parser")
        #print(soup)
        for link in soup.findAll("a", {"class" : "hdrlnk"}):
            #print(link)
            href = link.get("href")
            title = link.string
            print(title)
            print(href)
            get_single_item_data(href)
            print("\n\n\n\n\n\n")
        page += 1

def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for item_value in soup.findAll("span", {"class" : "price"}):
        print(item_value.string)
    # for item_info in soup.findAll("section", {"id" : "postingbody"}):
    #     print (item_info.text)
    # for link in soup.findAll("a", href=True):
    #     href = link.get("href")
    #     print(href)

web_scraper(1)


#hw // use this library to make a web scraper in any other website // save the info in a txt file
