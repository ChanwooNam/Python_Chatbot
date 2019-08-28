from flask import Flask
import random
import collections
import requests
app = Flask(__name__)

@app.route('/')
def home():
    return 'hello'

# 1. 주문서를 만들고.
# 2. 해당 주문이 들어왔을 때 무엇을 할지 정의

@app.route('/name')
def name():
    return '남찬우'

@app.route('/hello/<name>')
def hello(name):
    return f'hello {name}'

@app.route('/square/<int:number>')
def square(number):
    return str(number ** 2)

@app.route('/menu')
def menu():
    foods = ['바스버거', '대우식당', '진가와', '고갯마루']
    food = random.choice(foods)
    return food

@app.route('/lotto')
def lotto():
    #winner = [3, 5, 12, 13, 33, 39]

    # 1. requests 통해 요청 보내기
    url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=873'
    response = requests.get(url)
    res_dict = response.json()

    # 1등 번호 6개가 담긴 result라는 list를 출력.

    winner = []
    for i in range(1,7) :
        winner.append(res_dict[f'drwtNo{i}'])

    print(winner)

    lottoNumber = random.sample(range(1, 46) , 6)
    #lottoNumber = [3, 5, 12, 23, 32]
    cnt = len(set(winner) & set(lottoNumber))


    rank = '꽝'
    if cnt == 6:
        rank = '1등'
    elif cnt == 5:
        rank = '3등'
    elif cnt == 4:
        rank = '4등'
    elif cnt == 3:
        rank = '5등'
    # 만약 6개가 모두 일치하면 -> 1등
    # 만약 5개가 일치하면 -> 3등
    # 만약 4개가 일치하면 -> 4등
    # 만약 3개가 일치하면 -> 5등
    
    return str(sorted(lottoNumber)) + rank

