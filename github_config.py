import os

password = str(os.environ['WP_PASSWORD'])
user = str(os.environ['WP_USER'])
url = f"{os.environ['URL']}"
novel_name = str(os.environ['NOVEL_NAME'])
my_site = f"{os.environ['MY_SITE']}"
translation_site = str(os.environ['TRANSLATION_SITE'])
nu_username = str(os.environ['NU_USER'])
nu_password = str(os.environ['NU_PASSWORD'])
translator = str(os.environ['TRANSLATOR'])
special = ['[', ']', '\\', '\'', '!', '@', '#', '$', '%', '^', '&', '*','{', '}', '"', ':', ';', ',', '<', '>', '.', '?', '<WordPressPost: b\'', 'WordPressPost: ', '\'>']
tags = [os.environ['TAGS']]
name_edit = novel_name.lower().replace(" ", '-')
novel_link = f"{os.environ['NOVEL_LINK']}{name_edit}/"
