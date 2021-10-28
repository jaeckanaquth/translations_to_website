import os

password = str(os.environ['WP_PASSWORD'])
user = str(os.environ['WP_USER'])
url = f"{os.environ['URL']}"
print(password, user, url)
novel_name = str(os.environ['NOVEL_NAME'])
my_site = f"{os.environ['MY_SITE']}"
translation_site = str(os.environ['TRANSLATION_SITE'])
nu_username = str(os.environ['NU_USER'])
nu_password = str(os.environ['NU_PASSWORD'])
translator = str(os.environ['TRANSLATOR'])
special = ['[', ']', '\\', '\'', '!', '@', '#', '$', '%', '^', '&', '*','{', '}', '"', ':', ';', ',', '<', '>', '.', '?', '<WordPressPost: b\'', 'WordPressPost: ', '\'>']
tags = [os.environ['TAGS']]
novel_link = f"{str(os.environ['NOVEL_LINK'])}{novel_name.lower().replace(" ", '-')}/"
