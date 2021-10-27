import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
from config import url, novel_name, novel_link
from page_translator import page_publishandlink
from wordpress_post import uploadImage

def main_img():
    novel = requests.get(url)
    novel.raise_for_status()
    novel.encoding = "GBK"
    novelSoup = bs(novel.text, "html.parser")
    novel_img = novelSoup.findAll('img')
    novel_img = novel_img[0]['src']
    img_data = requests.get(novel_img).content
    return novel_img, img_data

def main():
    filename = novel_name.replace(" ", "-") + ".jpg"
    published = pd.DataFrame(columns=["name", "post_id", "link_id", "wp_link"])

    if filename not in published["name"].to_list():
        novel_img, img_data = main_img()
        img_id = uploadImage(novel_img, img_data)
        # img_id = 'abc'
        dct = {"name": filename, "post_id": img_id, "link_id": novel_img, "wp_link": novel_link + img_id}
        published = published.append(dct, ignore_index=True)
        print(published)
            
    #save novel chapters
    page_publishandlink(published)
    return 'done'

if __name__ == "__main__":
    main()
