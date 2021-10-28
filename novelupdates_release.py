from selenium.webdriver.support.ui import Select
from typing import NoReturn
from selenium import webdriver
import requests, glob
from bs4 import BeautifulSoup as bs
from time import sleep
if glob.glob("config.py"):
    from config import nu_username, nu_password, novel_name, translator
else:
    from github_config import nu_username, nu_password, novel_name, translator


def page_linktonu(release_link_url, header):
    url = "https://www.novelupdates.com/add-release/"
    login = "https://www.novelupdates.com/login/"

    myedge = "C:/Users/jaeck/Documents/personal_workspace/downloads/msedgedriver.exe"

    driver = webdriver.Edge(executable_path= myedge)
    driver.get(login)
    # sleep(30)
    username = driver.find_element_by_id("user_login")
    username.send_keys(nu_username)
    password = driver.find_element_by_id("user_pass")
    password.send_keys(nu_password)

    driver.find_element_by_name("wp-submit").click()

    driver.get(url)
    sleep(30)
    try:
        group = driver.find_element_by_id("group_change_100").clear()
        group = driver.find_element_by_id("group_change_100")
        group.send_keys(translator)
        sleep(30)
        group = driver.find_element_by_id("group_change_100")
        driver.find_element_by_class_name("change_list").click()

        release_link = driver.find_element_by_id("arlink")
        release_link.send_keys(release_link_url)

        title = driver.find_element_by_id("title_change_100").clear()
        title = driver.find_element_by_id("title_change_100")
        title.send_keys(novel_name)
        sleep(30)
        title = driver.find_element_by_id("title_change_100")
        driver.find_element_by_class_name("change_list").click()

        release_chapter = driver.find_element_by_id("arrelease")
        release_chapter.send_keys(header)

    except Exception as e:
        print("Error of NU:" + str(e))

    driver.find_element_by_name("submit").click()
    driver.close()
    return 'done'
