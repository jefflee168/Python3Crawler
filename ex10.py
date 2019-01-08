#-*- coding: utf-8 -*-

import requests

proxies = {
    "http": "http://10.0.0.103:8888",
}

requests.get("https://www.taobao.com", proxies=proxies)
