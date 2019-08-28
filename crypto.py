# [해커] Bithumb open API를 활용하여,
# 실시간 BTC(Bitcoin) 현재가를 출력하는 crypto.py

import requests

url = 'https://api.bithumb.com/public/ticker/BTC'
response = requests.get(url)
res_dict = response.json()

print(res_dict['data']['opening_price'])

