import requests, config
import lxml, os
from bs4 import BeautifulSoup as bs
from time import sleep
from deep_translator import GoogleTranslator
from wordpress_post import posting_draft

def page_translate(url):
    novel = requests.get(url)
    novel.raise_for_status()
    novel.encoding = "GBK"
    novelSoup = bs(novel.text, "html.parser")
    novel_content = novelSoup.find('div', id = 'content')
    novel_content = novel_content.get_text(strip=True, separator='\n')
    heading = novelSoup.find('h1')
    heading = heading.get_text(strip=True, separator='\n')
    # print(heading)

    text = '[unedited]' + '\n'
    for content in novel_content.split("\n"):
        # content = content.replace("*******", "-------进而---------")
        try:
            # sleep(10)
            translated = GoogleTranslator(source='auto', target='en').translate(content)
            # print(translated)
            text = text + '\n' + translated
        except Exception as e:
            e = str(e)
            if "can only concatenate str" in e:
                pass
            elif "otherwise it cannot be translated" in e:
                text = text + '\n' + content
            else:
                print(e)
                pass



    return text

def header(url):
    novel = requests.get(url)
    novel.raise_for_status()
    novel.encoding = "GBK"
    novelSoup = bs(novel.text, "html.parser")
    heading = novelSoup.find('h1')
    heading = heading.get_text(strip=True, separator='\n')
    
    header = ''
    for content in heading.split(" "):
        try:
            translated = GoogleTranslator(source='auto', target='en').translate(content)
            if header == '':
                header = translated
            else:
                header = header + " " + translated
        except Exception as e:
            print(e)
    return header

def page_saveandpublish(url, novel_name):
    if not os.path.exists(novel_name):
            os.makedirs(novel_name)
    novel = requests.get(url)
    novel.raise_for_status()
    novel.encoding = "GBK"
    novelSoup = bs(novel.text, "html.parser")
    page_lst = []
    novel_link = novelSoup.findAll('dd')
    for dd in novel_link:
        page_lst.append(dd.find('a')['href'])
    for page in sorted(page_lst):
        url = config.translation_site + page
        try:
            heading = header(url)
            if not os.path.exists(novel_name + "/" + heading + ".md"):
                content = page_translate(config.translation_site + page)
                with open(novel_name + "/" + heading + ".md", "w", encoding='utf-8') as text_file:
                    text_file.write(content)
                    text_file.close()
                print("posted:" + posting_draft(heading, content))
            print("Done:" + heading)
        except Exception as e:
            print(e)
            sleep(100)
