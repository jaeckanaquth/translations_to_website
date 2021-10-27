import os

password = str(os.getenv['WP_PASSWORD'])
user = str(os.getenv['WP_USER'])
url = str(os.getenv['URL'])
novel_name = str(os.getenv['NOVEL_NAME'])
my_site = str(os.getenv['MY_SITE'])
translation_site = str(os.getenv['TRANSLATION_SITE'])
nu_username = str(os.getenv['NU_USER'])
nu_password = str(os.getenv['NU_PASSWORD'])
translator = str(os.getenv['TRANSLATOR'])
special = list(os.getenv['SPECIAL'])
tags = list(os.getenv['TAGS'])
novel_link = str(os.getenv['NOVEL_LINK']) + \
    novel_name.lower().replace(" ", '-') + '/'
