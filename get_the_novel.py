#TODO: Get the novel from the website https://www.52shuku.vip and return it as a string

import requests
from bs4 import BeautifulSoup

def get_the_novel_pages(novel_page_url):
    url = "https://www.52shuku.vip/" + novel_page_url + ".html"
    print(url)
    response = requests.get(url)
    response.encoding = 'utf-8'  # Specify the correct encoding
    soup = BeautifulSoup(response.text, 'html.parser')
    novel = soup.find('div', class_='content')
    full_page = novel.text
    full_page = full_page.split("\n")
    for key, i in enumerate(full_page):
        if '页第2页第3页第4页第5' in i:
            last_key = key
            break
    last_page = full_page[last_key][-5:].replace("页","").replace("第","")
    # print(last_page)
    return int(last_page) + 1

def get_novel_page(novel_page_url, page_number):
    url = "https://www.52shuku.vip/" + novel_page_url + f"_{page_number}" + ".html" #https://www.52shuku.vip/chongsheng/24_b/bjUCn_2.html
    print(url)
    response = requests.get(url)
    response.encoding = 'utf-8'  # Specify the correct encoding
    soup = BeautifulSoup(response.text, 'html.parser')
    novel = soup.find('div', class_='content')
    full_page = novel.text
    #remove everything till 52书库App下载 | 阅读记录
    full_page = full_page.split("52书库App下载 | 阅读记录")
    # remove everything after 目录
    full_page = full_page[-1].split("目录")
    return full_page
