# class SuperMario:
#     def __init__(self):
#         self.pos = 0
#     def forward(self):
#         self.pos = self.pos + 20
#
# mario = SuperMario()
# mario.forward()
#
# print(f'{mario.pos}')
#
# class Mycass:
#     def add(self, a, b):
#         return a + b
#
# obj = Mycass()
# obj1 = Mycass()
# ret1 = obj1.add(70,9)
# ret = obj.add(3,4)
# print(f'{ret} {ret1}')
#
# class 붕어빵틀:
#     def 팥소넣기(self, 팥소):
#         self.팥소 = 팥소
#
# 붕어빵1 = 붕어빵틀()
#
# 붕어빵1.팥소넣기("초코맛팥소")
# print(f'{붕어빵1.팥소넣기}')


class Books:
    def __init__(self, title, other, yes24):
        self.title = title
        self.other = other
        self.yes24 = yes24

Books1 = Books("파친코", "이민진", "yes24")

print(f'제목: {Books1.title}\n저자: {Books1.other}\n출판사: {Books1.yes24}')

class Books2:
  pass
book3 = Books2(Books)
print(book3.title)
