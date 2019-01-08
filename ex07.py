#-*- coding: utf-8 -*-

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'
}

r = requests.get("https://www.zhihu.com/explorer", headers=headers)
print(r.text)
