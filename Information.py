import requests
from bs4 import BeautifulSoup
import shutil

search_term = "search term"
posts_scrape = requests.get(f"https://www.tumblr.com/search/{search_term}", stream=True)
soup = BeautifulSoup(posts_scrape.text, "html.parser")

articles = soup.find_all("article", class_="FtjPK")

data = {}
posts_scrape.raw.decode_content = True
for article in articles:
    try:
        source = article.find("div", class_="vGkyT").text
        for imgvar in article.find_all("img", alt="Image"):
            data.setdefault(source, []).extend(
                [
                    i.replace("500w", "").strip()
                    for i in imgvar["srcset"].split(",")
                    if "500w" in i
                ]
            )
    except AttributeError:
        continue

for source, image_urls in data.items():
    for url in image_urls:
        # make request with image url 
        img_scrape = requests.get(url, stream=True)

        if img_scrape.status_code == 200:
            with open(f"pics/{source}",'wb') as f:
                img_scrape.raw.decode_content = True
                
                # save the image raw format
                shutil.copyfileobj(img_scrape.raw, f)
            print('Image sucessfully Downloaded: ', source)
        else:
            print('Image Couldn\'t be retrieved')