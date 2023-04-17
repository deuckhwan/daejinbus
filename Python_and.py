

# bitcoin_ma5 = 1900
# bitcoin_price = 1939
# bitcoin_target = 1937
#
# if (bitcoin_price > bitcoin_ma5) and (bitcoin_price > bitcoin_target):
#     print(f'매수 상승장 입니다.')
#
# num1 = 10
# num2 = 30
#
# if num1 > num2:
#     print(f'{num1}이 {num2}작습니다.')
# elif num2 > num1:
#     print(f'{num2}이 {num1}큽니다.')

grades = int(input("점수를 입력하세요\n"))

if 90 <= grades < 100:
    print(f'A 학점')
elif 80 <= grades < 89:
    print(f'B 학점')
elif 70 <= grades < 79:
    print(f'C 학점')
elif 60 <= grades < 69:
    print(f'D 학점')
else:
    print(f'F 학점')