import requests
from bs4 import BeautifulSoup

def scrap_review_from_web(URL) :

    url = URL

    HEADER = ({'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36','Accept-Language':'eng-us, en;q=0.5'})

    website = requests.get(url,HEADER)
    soup = BeautifulSoup(website.text , "html.parser")

    review = soup.find('div', class_="a-expander-content reviewText review-text-content a-expander-partial-collapse-content").text

    print("🔴🔴🔴🔴🔴🔴🔴")
    print("🔴🔴🔴🔴🔴🔴🔴")
    print(f"{review}🟣🟣🟣🟣🟣")
    print("🔴🔴🔴🔴🔴🔴🔴")
    print("🔴🔴🔴🔴🔴🔴🔴")

    return(review)
