class Jss:
    def __init__(self):
        self.name = input("이름: ")
        self.age = input("나이: ")

    def show(self):
        print(f'이름:{self.name}\n나이:{self.age}세 입니다.')


a = Jss()
print(f'이름:{a.name}')
print(f'나이:{a.age}')
print(f'{a.show()}')