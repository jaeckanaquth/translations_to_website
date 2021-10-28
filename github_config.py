import os

password = str(os.environ['WP_PASSWORD'])
user = str(os.environ['WP_USER'])
url = f'https://www.mbtxt.la/go/91929/'
novel_name = "I Became a Heartthrob After A Job in Quick Transmigration"
my_site = f"{os.environ['MY_SITE']}"
translation_site = f'https://www.mbtxt.la/go/'
nu_username = str(os.environ['NU_USER'])
nu_password = str(os.environ['NU_PASSWORD'])
translator = str(os.environ['TRANSLATOR'])
special = ['[', ']', '\\', '\'', '!', '@', '#', '$', '%', '^', '&', '*','{', '}', '"', ':', ';', ',', '<', '>', '.', '?', '<WordPressPost: b\'', 'WordPressPost: ', '\'>']
tags = ['IBHAJQT']
name_edit = novel_name.lower().replace(" ", '-')
novel_link = f"{my_site}{name_edit}/"
