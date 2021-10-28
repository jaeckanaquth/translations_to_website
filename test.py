from urllib.request import Request, urlopen
import config

req = Request(config.url,
              headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
