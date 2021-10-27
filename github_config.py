import os

password = str(os.environ.get('WP_PASSWORD'))
user = str(os.environ.get('WP_USER'))
url = str(os.environ.get('URL'))
print(password, user, url)
novel_name = str(os.environ.get('NOVEL_NAME'))
my_site = str(os.environ.get('MY_SITE'))
translation_site = str(os.environ.get('TRANSLATION_SITE'))
nu_username = str(os.environ.get('NU_USER'))
nu_password = str(os.environ.get('NU_PASSWORD'))
translator = str(os.environ.get('TRANSLATOR'))
special = ['[', ']', '\\', '\'', '!', '@', '#', '$', '%', '^', '&', '*','{', '}', '"', ':', ';', ',', '<', '>', '.', '?', '<WordPressPost: b\'', 'WordPressPost: ', '\'>']
tags = [os.environ.get('TAGS')]
novel_link = str(os.environ.get('NOVEL_LINK')) + novel_name.lower().replace(" ", '-') + '/'
