import json
from os import name
import requests, glob
import gspread
import novel_scrap
import gspread_dataframe as gd
import pandas as pd
from bs4 import BeautifulSoup as bs
from update_sheet import updates
if glob.glob("config.py"):
    from config import url, novel_name, novel_link, name_edit
else:
    from github_config import url, novel_name, novel_link, name_edit, service_account
from page_translator import page_publishandlink
from wordpress_post import uploadImage
from requests.auth import HTTPBasicAuth

user_agent = {'User-Agent': 'Mozilla/5.0'}

if not glob.glob("service_account.json"):
    service_account = json.loads(service_account)
    with open('service_account.json', 'w') as f:
        json.dump(service_account, f)
gc = gspread.service_account(filename="service_account.json")

try:
    sh = gc.open("QuthsTranslations")
except:
    sh = gc.create("QuthsTranslations")

filename = novel_name.replace(" ", "-") + ".jpg"

try:
    worksheet = gc.open('QuthsTranslations').worksheet(name_edit)
    published = pd.DataFrame(worksheet.get_all_records())

except:
    worksheet = sh.add_worksheet(title=name_edit, rows="100", cols="4")
    published = pd.DataFrame(columns = ["name", "post_id", "link_id", "wp_link"])

if filename not in published["name"].to_list():
    novel_img, img_data = novel_scrap.main_img()
    img_id = uploadImage(novel_img, img_data)
    # img_id = 'abc'
    dct = {"name": filename, "post_id": img_id, "link_id": novel_img, "wp_link": ""}
    try:
        published = published.append(dct, ignore_index=True)
    except:
        published["name"] = "test"
        published["post_id"] = "test"
        published["link_id"] = "test"
        published["wp_link"] = "test"
        published = published.append(dct, ignore_index=True)
    gd.set_with_dataframe(worksheet, published)
    published = updates(published,worksheet)
    print(published)
        
#save novel chapters
page_publishandlink(published, worksheet)

