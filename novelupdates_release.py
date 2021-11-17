from selenium import webdriver
import glob
from time import sleep
if glob.glob("config.py"):
    from config import nu_username, nu_password
    import nu_config
else:
    from github_config import nu_username, nu_password


def page_linktonu(release_link_url, header):
    url = "https://www.novelupdates.com/add-release/"
    login = "https://www.novelupdates.com/login/"

    driver = webdriver.Edge(
        executable_path="C:/Users/jaeck/Documents/personal_workspace/downloads/msedgedriver.exe")
    driver.get(login)
    # sleep(30)
    username = driver.find_element_by_id("user_login")
    username.send_keys(nu_username)
    password = driver.find_element_by_id("user_pass")
    password.send_keys(nu_password)

    driver.find_element_by_name("wp-submit").click()

    driver.get(url)
    sleep(30)

    group = driver.find_element_by_id("group_change_100").clear()
    group = driver.find_element_by_id("group_change_100")
    group.send_keys(nu_config.translator)
    sleep(15)
    group = driver.find_element_by_id("group_change_100")
    driver.find_element_by_class_name("change_list").click()

    release_link = driver.find_element_by_id("arlink")
    release_link.send_keys(release_link_url)

    title = driver.find_element_by_id("title_change_100").clear()
    title = driver.find_element_by_id("title_change_100")
    title.send_keys(nu_config.novel_name)
    sleep(30)
    title = driver.find_element_by_id("title_change_100")
    driver.find_element_by_class_name("change_list").click()

    release_chapter = driver.find_element_by_id("arrelease")
    release_chapter.send_keys(header)

    driver.find_element_by_name("submit").click()
    driver.close()
    return 'done'


if glob.glob("nu_config.py"):
    page_linktonu(nu_config.release_link_url, nu_config.header)
