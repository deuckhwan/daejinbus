class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def mul(self):
        result = self.first - self.second
        return result

    def sub(self):
        result = self.first * self.second
        return result

    def div(self):
        result = self.first / self.second
        return result

a = FourCal(3, 4)
print(a.add())

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

class SafeFourCal(FourCal):

    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second


a = MoreFourCal(4, 4)
print(f'{a.pow()}')

a = SafeFourCal(2, 1)
print(a.div())

