class BlackBox:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def set_travel_mode(self, min):
        print(f'{self.name} {min}분 동안 여행 모드 ON')

b1 = BlackBox('까망이', 200000)
b2 = BlackBox('하양이', 100000)

b1.set_travel_mode(20)
b2.set_travel_mode(10)