import json
import pandas as pd
import requests
import lxml.html
import sys
from dotenv import load_dotenv
import os
from bs4 import BeautifulSoup

# Load environment variables from .env file
load_dotenv()

def login():
    # Get credentials from environment variables
    username = os.getenv('NU_USERNAME')
    password = os.getenv('NU_PASSWORD')

    if not username or not password:
        print("Error: Credentials not found in .env file")
        sys.exit()

    return username, password

def log_into(username, password):
    print("\tLogging in to NovelUpdates")
    s = requests.session()

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
    }

    response = s.get('https://www.novelupdates.com/login/', headers=headers, timeout=5)
    if response.status_code == 200:
        login_html = lxml.html.fromstring(response.text)
        hidden_inputs = login_html.xpath(r'//form//input[@type="hidden"]')
        form = {x.attrib["name"]: x.attrib["value"] for x in hidden_inputs}
        form['log'] = username
        form['pwd'] = password
        response = s.post('https://www.novelupdates.com/login/', data=form, headers=headers)

        if response.url == 'https://www.novelupdates.com/':
            print("\t  ===Login Success===")
            return s
        else:
            print("Error: Unable to log on, please check credentials")
            sys.exit()
    else:
        print(f"Failure to access login page, status code: {response.status_code}")
        sys.exit()

def submit_release(session, series_id, chapter, link, group_id, release_date):
    pass

  


def nu_post_chapter(data):
  username, password = login()
  session = log_into(username, password)
  
  # Chapter data
  series_id = data["series_id"]
  chapter = data["Chapter"]
  link = data["post url"]
  group_id = "techTaleWorld"
  release_date = data["post date"]
  
  submit_release(session, series_id, chapter, link, group_id, release_date)

# nu_post_chapter({
#         "name": "Survival Wen Male Match [Fast Wear]_ Laughing Halo Xi Shi [End + Extra]",
#         "url": "https://www.52shuku.vip/chongsheng/26_b/bjVDv.html",
#         "posted": "no",
#         "breakoff page": 27,
#         "last page": 121,
#         "series_id": "Survival Male Supporting Role [Quick Transmigration]",
#         "post url": "https://translations.techtaleworld.com/survival-male-supporting-role-[quick-transmigration]/chapter-smsrt_25",
#         "Chapter": "c25",
#         "post date": "11/28/24"
#     })


def save_to_csv(data, df):

    df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
    # Save the DataFrame to a CSV file
    df.to_csv(f'novels/all_links/{data["series_id"]}.csv', index=False)
    return df
