import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

user_agent = {'User-Agent': 'Mozilla/5.0'}


def updates(df, worksheet):
    try:
        for url, name in zip(df['wp_link'].to_list(), df['name'].to_list()):
            novel = requests.get(url, headers=user_agent)
            novelSoup = bs(novel.text, "html.parser")
            heading = novelSoup.find("h1", {"class": "entry-title"})
            heading = heading.get_text(strip=True, separator='\n')
            worksheet.update('A1', [name, heading])
            published = pd.DataFrame(worksheet.get_all_records())
            return published
    except:
        print("Done for!!")

