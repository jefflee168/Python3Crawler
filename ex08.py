#-*- coding: utf-8 -*-

import requests

files = {'file': open('ex01.py','rb')}
r = requests.post("http://www.hao1314.tech/post",files=files)
print(r.text)
