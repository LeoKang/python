class Data:
    def __init__(self, h, w):
        self.h = int(h)
        self.w = float(w)

    def __add__(self, other):
        return Data(self.h + other.h, self.w + other.w)

p1 = Data(*input("당신의 키와 몸무게를 입력하세요.").split())
p2 = Data(*input("친구의 키와 몸무게를 입력하세요.").split())

p1_plus_p2 = p1 + p2

print(f"my 키: {p1.h}, 몸무게: {p1.w:.1f}")
print(f"friend 키: {p2.h}, 몸무게: {p2.w:.1f}")
print(f"plus 키: {p1_plus_p2.h}, 몸무게: {p1_plus_p2.w:.1f}")
# 3. -------------------------------------
class Person:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def __add__(self, other):
        return Person(self.height + other.height, self.weight + other.weight)
    def __sub__(self, other):
        return Person(abs(self.height - other.height), abs(self.weight - other.weight))
    def __truediv__(self, num):
        return Person(self.height / num, self.weight / num)
    def __floordiv__(self, num):
        return Person(self.height // num, self.weight / num)
    def __str__(self):
        return f"키: {self.height}, 몸무게: {self.weight:.1f}"

h1, w1 = input("당신의 키와 몸무게를 입력하세요.").split()
h2, w2 = input("친구의 키와 몸무게를 입력하세요.").split()

p1 = Person(int(h1), float(w1))   
p2 = Person(int(h2), float(w2))

print("my", p1)
print("friend", p2)
print("plus", p1 + p2)
print("minus", p1 - p2)
print("avg", (p1 + p2) // 2)
# 3. -----------------------------------------------

class Body:
    def __init__(self, name, hi, wei):
        self.name = name
        self.hi = int(float(hi))
        self.wei = float(wei)

    def __add__(self, other):
        return Body("plus", self.hi + other.hi, self.wei + other.wei)

    def __sub__(self, other):
        return Body("minus", abs(self.hi - other.hi), abs(self.wei - other.wei))

    def __truediv__(self, other):
        return Body("avg", (self.hi + other.hi) // 2, (self.wei + other.wei) / 2)

    def __str__(self):
        return f"{self.name} 키: {self.hi}, 몸무게: {self.wei:.1f}"

line1 = input("당신의 키와 몸무게를 입력하세요.").split()
m_h = line1[-2].split('.')[-1]
m_w = line1[-1]
me = Body("my", m_h, m_w)

line2 = input("친구의 키와 몸무게를 입력하세요.").split()
f_h = line2[-2].split('.')[-1]
f_w = line2[-1]
fr = Body("friend", f_h, f_w)

results = [me, fr, me + fr, me - fr, me / fr]

for res in results:
    print(res)
# 2. --------------------------------------------------
class Person:
    def __init__(self, cm, kg):
        self.cm = int(cm)
        self.kg = kg
    def __add__(self, other):
        # print("plus 키:", self.cm + other.cm, ", 몸무게: ", self.kg + other.kg)
        print(f"plus 키: {self.cm + other.cm}, 몸무게: {self.kg + other.kg}")
    def __sub__(self, other):
        print("minus 키:", abs(self.cm - other.cm), end='')
        print(f", 몸무게: {abs(p1.kg - p2.kg):.1f}")
    def __truediv__(self, other):
        print(f"avg 키: {int((self.cm + other.cm)/2)}, 몸무게: {((self.kg + other.kg)/2):.1f}")
    def __str__(self):
        return  f"키: {self.cm}, 몸무게: {self.kg:.1f}"
        
cm, kg = map(float, input("당신의 키와 몸무게를 입력하세요.").split())
p1 = Person(cm, kg)

cm, kg = map(float, input("친구의 키와 몸무게를 입력하세요.").split())
p2 = Person(cm, kg)

print("my", p1)
print("friend", p2)
p1 + p2
p1 - p2
p1 / p2