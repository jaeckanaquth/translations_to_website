from environs import Env

env = Env()

password = str(env('WP_PASSWORD'))
user = str(env('WP_USER'))
url = str(env('URL'))
print(password, user, url)
novel_name = str(env('NOVEL_NAME'))
my_site = str(env('MY_SITE'))
translation_site = str(env('TRANSLATION_SITE'))
nu_username = str(env('NU_USER'))
nu_password = str(env('NU_PASSWORD'))
translator = str(env('TRANSLATOR'))
special = ['[', ']', '\\', '\'', '!', '@', '#', '$', '%', '^', '&', '*','{', '}', '"', ':', ';', ',', '<', '>', '.', '?', '<WordPressPost: b\'', 'WordPressPost: ', '\'>']
tags = [str(env('TAGS'))]
novel_link = str(env('NOVEL_LINK')) + novel_name.lower().replace(" ", '-') + '/'
