# def hep(a, b):
#     ret = a + b
#     return ret
#
# result = hep(3, 4)
# result1 = hep(10, 20)
# print(f'{result1}')
# print(f'{result}')
#
# ohlc = [100, 200, 300, 400]
# def print_ohlc(ohlc):
#     print(f'시가: {ohlc[0]}\n고가: {ohlc[1]}\n저가: {ohlc[2]}\n종가: {ohlc[3]}')
#
#
# print_ohlc(ohlc)
# ticker = "Pi"
# def get_min_order(ticker):
#     min_order = None
#
#     if ticker == "ETC":
#         min_order = 0.1
#
#     elif ticker == "ETH":
#         min_order = 0.5
#     elif ticker == "BTC":
#         min_order = 0.01
#     elif ticker == "XRP":
#         min_order = 10
# #     else:
#         min_order = 0.005
# #
# #     return min_order
# # min_order = get_min_order("BTC")
# # print(f'수수료: {min_order}')
# #
# # def 별찍기():
# #     print(f'*' * 40)
# #     print(f'*' * 40)
# #
# # 별찍기()
# #
# # def mygop(a, b):
# #
# #     gop_hap = a * b
# #     return gop_hap
# # gop_hap = mygop(9, 9)
# # gop_hap1 = mygop(18, 6)
# # print(f'{gop_hap1}')
# # print(gop_hap)
# #
# # def so_ticker(ticker):
# #
# #     lave = ticker.upper()
# #
# #     return lave
# # lave = so_ticker("btc")
# # print(f'{lave}')

def picup_even(numbers):
    even = [ ]
    for number in numbers:
        if number % 2 == 0:
            even.append(number)

    return even

even = picup_even([1,3,5,6,90,100,120])
print(even)