import requests
from bs4 import BeautifulSoup
import pandas as pd
 
def scrap_review(URL) :

    url = URL

    HEADER = ({'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36','Accept-Language':'eng-us, en;q=0.5'})

    website = requests.get(url,HEADER)
    soup = BeautifulSoup(website.text , "html.parser")

    review = soup.find('p', class_="a-spacing-small").text

    print("🔴🔴🔴🔴🔴🔴🔴")
    print("🔴🔴🔴🔴🔴🔴🔴")
    print(f"{review}did it work")
    print("🔴🔴🔴🔴🔴🔴🔴")
    print("🔴🔴🔴🔴🔴🔴🔴")

    return(review)

   

scrap_review('https://www.amazon.com/Snpurdiri-Keyboard-Ultra-Compact-Waterproof-Black-White/dp/B097T276QL/ref=sr_1_1_sspa?_encoding=UTF8&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY')