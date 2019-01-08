# -*- coding: utf-8 -*-

import urllib.request

response = urllib.request.urlopen('https://www.python.org')
print('状态码为：',response.status)
print(response.getheaders())
print('Web 服务器为：',response.getheader('Server'))
