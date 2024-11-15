from amazon_scraper import scrap_review_from_web
from review_generator import generate_costum_review

url = 'https://www.amazon.com/Disney-Cars-Collection-Character-Collectible/dp/B09BW56L6V/ref=slsr_d_dpds_fsdp4star_fa_xcat_cheapdynam_d_sccl_2_2/145-0775674-3399269'

prompt_from_user = f"Summarize and personalize the review:"

review_from_web = scrap_review_from_web(url)

generate_costum_review(review_from_web,prompt_from_user)


