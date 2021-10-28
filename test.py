import config
import requests
from requests_toolbelt.utils import dump


def print_raw_http(response):
    data = dump.dump_all(response, request_prefix=b'', response_prefix=b'')
    print('\n' * 2 + data.decode('utf-8'))


headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_2 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B202 NETGEAR/v1 (iOS Vuezone)',
}
session = requests.Session()
r = session.options(config.url, headers=headers)
print_raw_http(r)
r.raise_for_status()
