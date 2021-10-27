import os

password = str(os.environ['WP_PASSWORD'])
user = str(os.environ['WP_USER'])
url = str(os.environ['URL'])
novel_name = str(os.environ['NOVEL_NAME'])
my_site = str(os.environ['MY_SITE'])
translation_site = str(os.environ['TRANSLATION_SITE'])
nu_username = str(os.environ['NU_USER'])
nu_password = str(os.environ['NU_PASSWORD'])
translator = str(os.environ['TRANSLATOR'])
special = list(os.environ['SPECIAL'])
tags = list(os.environ['TAGS'])
novel_link = str(os.environ['NOVEL_LINK']) + \
    novel_name.lower().replace(" ", '-') + '/'
