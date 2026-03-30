class BlackBox:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def set_travel_mode(self, min):
        print(str(min) + '분 동안 여행 모드 ON')

b1 = BlackBox('까망이', 200000)
b1.set_travel_mode(25)