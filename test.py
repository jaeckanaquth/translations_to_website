from urllib.request import urlopen, Request
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
reg_url = 'https://www.shubaow.net/211_211977/'
req = Request(url=reg_url, headers=headers)
html = urlopen(req).read()
print(html)
