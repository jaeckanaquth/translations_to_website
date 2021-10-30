import glob
if glob.glob("config.py"):
    import config
else:
    import github_config as config
import requests
from bs4 import BeautifulSoup as bs

user_agent = {'User-Agent': 'Mozilla/5.0'}

def page_scrap():
    if "www.mbtxt.la" in config.url:
        novel = requests.get(config.url, headers=user_agent)
        novel.raise_for_status()
        novel.encoding = "GBK"
        novelSoup = bs(novel.text, "html.parser")
        page_lst = []
        novel_link = novelSoup.findAll('dd')
        for dd in novel_link:
            page_lst.append(dd.find('a')['href'])
        return page_lst
    elif "imiaobige.com" in config.url:
        novel = requests.get(config.url, headers=user_agent)
        novel.raise_for_status()
        novel.encoding = "GBK"
        novelSoup = bs(novel.text, "html.parser")
        page_lst = []
        novel_link = novelSoup.findAll("a", {"class": "biaot"})
        for dd in novel_link:
            dd.get('href')
        return page_lst

def header_scrap(url):
    if "www.mbtxt.la" in config.url:
        novel = requests.get(url, headers=user_agent)
        novel.raise_for_status()
        novel.encoding = "GBK"
        novelSoup = bs(novel.text, "html.parser")
        heading = novelSoup.find("li", {"class": "active"})
        heading = heading.get_text(strip=True, separator='\n')
        return heading
    elif "imiaobige.com" in config.url:
        novel = requests.get(url, headers=user_agent)
        novel.raise_for_status()
        novel.encoding = "GBK"
        novelSoup = bs(novel.text, "html.parser")
        heading = novelSoup.find("h1")
        heading = heading.get_text(strip=True, separator='\n')
        return heading

def text_scrap(url):
    if "www.mbtxt.la" in config.url:
        novel = requests.get(url, headers=user_agent)
        novel.raise_for_status()
        novel.encoding = "GBK"
        novelSoup = bs(novel.text, "html.parser")
        novel_content = novelSoup.find("div", {"class": "readcontent"})
        novel_content = novel_content.get_text(strip=True, separator='\n')
        novel_content = novel_content.replace('AD4', '').replace('\\n', '\n').replace('\x1a', '')
        return novel_content
    elif "imiaobige.com" in config.url:
        novel = requests.get(url, headers=user_agent)
        novel.raise_for_status()
        novel.encoding = "GBK"
        novelSoup = bs(novel.text, "html.parser")
        novel_content = novelSoup.find("div", {"id": "content"})
        novel_content = novel_content.get_text(strip=True, separator='\n')
        novel_content = novel_content.replace('AD4', '').replace('\\n', '\n').replace('\x1a', '')
        return novel_content


def main_img():
    if "www.mbtxt.la" in config.url:
        session = requests.Session()
        novel = session.get(config.url, headers=user_agent)
        novel.raise_for_status()
        print(novel.status_code)
        novel.encoding = "GBK"
        novelSoup = bs(novel.text, "html.parser")
        novel_img = novelSoup.find("img", {"class": "thumbnail"})
        novel_img = novel_img['src']
        img_data = requests.get(novel_img).content
        return novel_img, img_data
    elif "imiaobige.com" in config.url:
        session = requests.Session()
        url = config.url[:-1] + ".html"
        novel = session.get(url, headers=user_agent)
        novel.raise_for_status()
        print(novel.status_code)
        novel.encoding = "GBK"
        novelSoup = bs(novel.text, "html.parser")
        novel_img = novelSoup.find("img")
        novel_img = novel_img['src']
        img_data = requests.get(novel_img).content
        return novel_img, img_data
