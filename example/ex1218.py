class BlackBox:
    def __init__(self, name, price):
        self.name = name
        self.price = price

b1 = BlackBox('까망이', 200000)
print(b1.name, b1.price)
b2 = BlackBox('하양이', 100000)
print(b2.name, b2.price)