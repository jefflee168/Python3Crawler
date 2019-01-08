#-*- coding: utf-8 -*-

import requests

response = requests.get('https://www.baidu.com', verify=False)
print(response.status_code)
