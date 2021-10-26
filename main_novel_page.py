import requests
import lxml, urllib
from bs4 import BeautifulSoup as bs
from time import sleep
import os
from wordpress_post import uploadImage
from page_translator import page_saveandpublish
from config import url, novel_name
from PIL import Image
import PIL
import os
import glob

if not os.path.exists(novel_name):
    os.mkdir(novel_name)

#save novel image
filename = novel_name + "/" + novel_name.replace(" ", "_") + ".jpg"
if not os.path.exists(filename):
    novel = requests.get(url)
    novel.raise_for_status()
    novel.encoding = "GBK"
    novelSoup = bs(novel.text, "html.parser")
    novel_img = novelSoup.findAll('img')
    novel_img = novel_img[0]['src']
    img_data = requests.get(novel_img).content
    with open(filename, 'wb') as img:
        img.write(img_data)
        
#save novel chapters
page_saveandpublish(url, novel_name)
