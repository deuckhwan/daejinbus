import datetime

num = 24 # 이틀전 순번 입력
order = 0 # 순서 번호
month_end = 58 # 30일 기준 29 or 58
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
today = datetime.date.today()
r = datetime.datetime.today().weekday()
print(f'#### 날 짜 ##### 요 일 #### 순 번 ####')
print(f'==============================')
while True:
    num += 11

    if num > 9 and num < 21:
        order += 1
        num += 10
        print(f'{today}일 {days[r]} {num}:번 ({r}) ')
        print(f'============================')
        today += datetime.timedelta(+1)
        r += 1
        for i in range(month_end):
            if r >= 7:
                r -= 7
    elif order > month_end: # 29 = 31일
        break
    elif num == 41:
        num -= 1
        continue
    elif num == 40:
        num -= 1
        continue
    elif num >= 30:
        num -= 30
        order += 1
        print(f'{today}일 {days[r]} {num}:번 ({r})')
        print(f'==============================')
        today += datetime.timedelta(+1)
        r += 1
        for i in range(month_end):
            if r >= 7:
                r -= 7




