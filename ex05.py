# -*- coding: utf-8 -*-

from urllib import request, error
try:
    response = request.urlopen('https://www.baidu.com/33.html')
except error.HTTPError as e:
    print(e.reason,e.code,e.headers,seq='\n')
