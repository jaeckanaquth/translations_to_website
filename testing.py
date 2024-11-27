from datetime import date, datetime, timedelta
import json

a = date.today() + timedelta(days=5)
a = str(a.strftime('%m/%d/%y'))
print(a)


with open('nu_all_tags.json', 'r') as file:
    seo_tags = json.load(file)

print(type(seo_tags))
