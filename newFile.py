import requests
from bs4 import BeautifulSoup
from huggingface_hub import InferenceClient
from huggingface_hub import login
import json 
login(token="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")
 
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



def generate_costum_review(review,prompt):
    given_review = review
    given_prompt = f'{prompt}{given_review}'

    generator = InferenceClient(model='microsoft/Phi-3-mini-4k-instruct', timeout=120)

    generated_respo = generator.post(
        json={
            'inputs' : given_prompt,
            'parameters':{'max_new_tokens' : 50},
            'task' : 'text-generation'
        }
    )

    res = json.loads(generated_respo.decode())[0]["generated_text"]
    res = res[len(prompt):]
    res = res[len(review):]

    print("🟢🟢🟢🟢🟢🟢🟢")
    print("🔴🔴🔴🔴🔴🔴🔴")
    print("🔴🔴🔴🔴🔴🔴🔴")
    print(f"{res}      did it ")
    print("🔴🔴🔴🔴🔴🔴🔴")
    print("🔴🔴🔴🔴🔴🔴🔴")

    return res


review_from_web = scrap_review('https://www.amazon.com/Snpurdiri-Keyboard-Ultra-Compact-Waterproof-Black-White/dp/B097T276QL/ref=sr_1_1_sspa?_encoding=UTF8&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY')

prompt_from_user = f"Summarize and personalize the review:"

generate_costum_review(review_from_web,prompt_from_user)
