#-*- coding: utf-8 -*-

from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

proxy_handler = ({
    'http': 'http://10.0.0.103:8888',
    #'https': 'https://10.0.0.103:8888',
})

opener = build_opener(proxy_handler)
try:
    response = opener.open('https://www.baidu.com')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)
