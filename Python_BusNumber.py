

 # 해운대 버스노선 순번 돌려보기

i = 1
while True:
    if i <= 31:
        print(f'순번: {i}번째')
        i += 11
        if i >= 31:
            i -= 30

        if i == 1:
            break