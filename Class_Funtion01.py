#       클래스 용어 정리
#      용 어        설 명
#      클래스      재품의 설계도
#       객 체      설계도로 만든 재품
#       속 성     클래스 안의 변수
#       메서드     클래스 안의 함수
#       생성자     객체를 만들때 실행되는 함수
#       인스턴스    메모리를 살아있는 객체(클래스에 포함된 객체)

class Moster: # 클래스 이름
    def __init__(self, name, age, addr): # 생성자 매개변수
        self.name = name
        self.age = age
        self.addr = addr
    def say(self): # 실행함수 메서드
        print(f'이름:{self.name} 나이:{self.age}세 주소:{self.addr} 입니다.')

proflie = Moster("박득환", 51, "신반송로196")
address = Moster("박재현", 23, "동래구명장동")
proflie.say()
address.say()
