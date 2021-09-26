import requests
import lxml, urllib
from bs4 import BeautifulSoup as bs
from time import sleep
import os
from wordpress_post import uploadImage
from page_translator import page_saveandpublish
import config

url = config.url
novel_name = config.novel_name

#save novel image
if not os.path.exists(novel_name + "/" + novel_name.replace(" ", "_") + ".jpg"):
    novel = requests.get(url)
    novel.raise_for_status()
    novel.encoding = "GBK"
    novelSoup = bs(novel.text, "html.parser")
    novel_img = novelSoup.findAll('img')
    novel_img = novel_img[0]['src']
    img_data = requests.get(novel_img).content
    with open(novel_name + "/" + novel_name.replace(" ", "_") + ".jpg", 'wb') as handler:
        handler.write(img_data)
    print(uploadImage(novel_name + "/" + novel_name.replace(" ", "_") + ".jpg"))
#save novel chapters
page_saveandpublish(url, novel_name)
