import glob
if glob.glob("config.py"):
    import config
else:
    import github_config as config
import requests
from bs4 import BeautifulSoup as bs

user_agent = {'User-Agent': 'Mozilla/5.0'}


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
    elif "yawen.cc" in config.url:
        session = requests.Session()
        url = config.url
        novel = session.get(url, headers=user_agent)
        novel.raise_for_status()
        print(novel.status_code)
        novel.encoding = "GBK"
        novelSoup = bs(novel.text, "html.parser")
        novel_img = novelSoup.find("img")
        novel_img = "https:" + novel_img['src']
        img_data = requests.get(novel_img).content
        return novel_img, img_data
    elif "jjwxc.net" in config.url:
        session = requests.Session()
        url = config.url
        novel = session.get(url, headers=user_agent)
        novel.raise_for_status()
        print(novel.status_code)
        novel.encoding = "GBK"
        novelSoup = bs(novel.text, "html.parser")
        novel_img = novelSoup.find("img")
        novel_img = "https:" + novel_img['src']
        img_data = requests.get(novel_img).content
        return novel_img, img_data

def page_scrap():
    if "www.mbtxt.la" in config.url:
        novel = requests.get(config.url, headers=user_agent)
        novel.raise_for_status()
        novel.encoding = "GBK"
        novelSoup = bs(novel.text, "html.parser")
        page_lst = []
        novel_link = novelSoup.findAll('dd')
        for dd in novel_link:
            url = config.url + str(dd.find('a')['href'])
            page_lst.append(url)
        return page_lst
    elif "yawen.cc" in config.url:
        novel = requests.get(config.url, headers=user_agent)
        novel.raise_for_status()
        novel.encoding = "GBK"
        novelSoup = bs(novel.text, "html.parser")
        page_lst = []
        novel_link = novelSoup.find_all("div", {"id": "list"})
        novel_link = novel_link[0].find_all("dd")
        for dd in novel_link:
            url = config.translation_site + dd.find('a')['href']
            page_lst.append(url)
        return page_lst
    elif "jjwxc.net" in config.url:
        novel = requests.get(config.url, headers=user_agent)
        novel.raise_for_status()
        novel.encoding = "GBK"
        novelSoup = bs(novel.text, "html.parser")
        page_lst = []
        novel_link = novelSoup.find_all("table", {"class": "cytable"})
        novel_link = novel_link[0].find_all("div", {"style": "float:left"})
        for dd in novel_link:
            try:
                url = dd.find('a')['href']
                page_lst.append(url)
            except:
                pass
        # print(page_lst)
        return page_lst

def header_scrap(url):
    if "www.mbtxt.la" in config.url:
        novel = requests.get(url, headers=user_agent)
        novel.raise_for_status()
        novel.encoding = "GBK"
        novelSoup = bs(novel.text, "html.parser")
        heading = novelSoup.find("h1", {"class": "pt10"})
        heading = heading.get_text(strip=True, separator='\n')
        heading = heading.replace("\n", "")
        return heading
    elif "yawen.cc" in config.url:
        novel = requests.get(url, headers=user_agent)
        novel.raise_for_status()
        novel.encoding = "GBK"
        novelSoup = bs(novel.text, "html.parser")
        heading = novelSoup.find("div", {"class": "bookname"})
        heading = heading.find("h1")
        heading = heading.get_text(strip=True, separator='\n')
        return heading
    elif "jjwxc.net" in config.url:
        novel = requests.get(url, headers=user_agent)
        novel.raise_for_status()
        novel.encoding = "GBK"
        novelSoup = bs(novel.text, "html.parser")
        heading = novelSoup.find("div")
        heading = novelSoup.find("h2")
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
    elif "yawen.cc" in config.url:
        novel = requests.get(url, headers=user_agent)
        novel.raise_for_status()
        novel.encoding = "GBK"
        novelSoup = bs(novel.text, "html.parser")
        novel_content = novelSoup.find("div", {"id": "content"})
        novel_content = novel_content.get_text(strip=True, separator='\n')
        novel_content = novel_content.replace(
            'AD4', '').replace('\\n', '\n').replace('\x1a', '')
        return novel_content
    elif "jjwxc.net" in config.url:
        novel = requests.get(url, headers=user_agent)
        novel.raise_for_status()
        novel.encoding = "GBK"
        novelSoup = bs(novel.text, "html.parser")
        novel_content = novelSoup.find("div", {"class": "noveltext"})
        # novel_content = novel_content.find_all("font")
        novel_content = novel_content.get_text(strip=True, separator='\n')
        novel_content = novel_content.replace(
            'AD4', '').replace('\\n', '\n').replace('\x1a', '').replace("�", "")
        return novel_content
