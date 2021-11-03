import glob
import requests
if glob.glob("config.py"):
    import config
else:
    import github_config as config
import gspread_dataframe as gd
from bs4 import BeautifulSoup as bs
import novel_scrap
from deep_translator import GoogleTranslator
from wordpress_post import posting, posting_test


def page_translate(url):

    novel_content = novel_scrap.text_scrap(url)

    text = '[unedited]' + '\n'
    for content in novel_content.split("\n"):
        try:
            translated = GoogleTranslator(source='auto', target='en').translate(content)
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

def header_name(url):
    heading = novel_scrap.header_scrap(url)
    header = ''
    for content in heading.split(" "):
        try:
            translated = GoogleTranslator(source='auto', target='en').translate(content)
            if header == '':
                header = translated
            else:
                header = header + " " + translated
            if header[-1] == ")":
                
                header = header.split(" ")
                heading = ''
                for i in header:
                    if heading == '':
                        heading = i
                    else:
                        heading = heading + " " + i
                header = heading
        except Exception as e:
            print(e)
    [header.replace(i, '') for i in config.special]
    return header


def page_publishandlink(df, worksheet):
    page_lst = novel_scrap.page_scrap()
    for url in sorted(page_lst):
        
        try:
            heading = header_name(url)
            print(heading)
            test = posting_test(heading, df)
            print(test)
            if test == "Need to be posted":
                content = page_translate(url)                    
                # whoops, I forgot to publish it!
                publish_id = posting(heading, content)
                #also need to put it on NU
                # print(page_linktonu(config.novel_link + publish_id, 'c' + str(df.shape[0] + 1)))
                head = heading.replace(
                    "(", "").replace(")", "").replace(" ", "-") + "/"
                dct = {"name": heading, "post_id": publish_id,
                       "link_id": url, "wp_link": config.novel_link + head.lower()}
                df = df.append(dct, ignore_index=True)
                gd.set_with_dataframe(worksheet, df)
                print(df)
                break
        except Exception as e:
            print("Error in Publishing: " + str(e))
            exit()
    return df
