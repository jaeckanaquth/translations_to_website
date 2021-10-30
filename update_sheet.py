import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import gspread_dataframe as gd

user_agent = {'User-Agent': 'Mozilla/5.0'}


def updates(df, worksheet):
    for url, name in zip(df['wp_link'].to_list(), df['name'].to_list()):
        # print(url)
        try:
            novel = requests.get(url, headers=user_agent)
            novelSoup = bs(novel.text, "html.parser")
            heading = novelSoup.find("h1", {"class": "entry-title"})
            heading = heading.get_text(strip=True, separator='\n')
            df.loc[df['name'] == name, 'name'] = heading
            print("Done for!! " + name + ": and did it to :" + heading)
        except:
            print("Done for!! " + name + " and could not do it")
    try:
        gd.set_with_dataframe(worksheet, df)
        return df
    except:
            print("Could not do it!!")


