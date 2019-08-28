"""
python으로 telegram message 보내기
"""

import requests

base_url ='https://api.telegram.org'
token = '나의 토큰id'

# (1) getUpdates를 통해 chat_id를 가져오자 
url = f'{base_url}/bot{token}/getUpdates'

response = requests.get(url)
res_dict = response.json()
print(res_dict)
chat_id = res_dict['result'][0]['message']['chat']['id']

# (2) url을 조합하여 requests로 요청 보내기 
text = '언제 금요일'
url = f'{base_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}'

print(url)
requests.get(url)