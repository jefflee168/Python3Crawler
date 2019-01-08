#-*- coding: utf-8 -*-

# 获取 github 的图标

import requests

r = requests.get("https://www.github.com/favicon.ico")
print(r.text)
print(r.content)
