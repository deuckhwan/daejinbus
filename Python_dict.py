# dict 딕셔너리 키값 밸류 값
price = { }

price['BTC'] = 21000000
price['XRP'] = 400
price['ETH'] = 2000000

del price["XRP"] # 딕셔너리 리스트 삭제

price["XRP"] = 300 # 딕셔너리 value값 변경

print(f'{price["BTC"], price["ETH"], price["XRP"]}') # 딕셔너리 value값 list 가지고오기

print(f'{price.keys()}')# 딕셔너리 key값 List 가지고 오기

print(f'{price.values()}') # 딕셔너리 value값 List 가지고 오기

# 연습문제

reple_data = {"02/21": 800, "02/22": 900, "02/23": 950, "02/24": 970, "02/25": 980}

ma5 = sum(reple_data.values())/5

print(f'리플데이터: {reple_data}\n리플5일 평균이동선: {ma5}')