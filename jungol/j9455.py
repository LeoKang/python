class Cir:
    def __init__(self,harf,pi):
        self.harf=harf
        self.pi=pi

    def cla(self):
        return ((self.harf**2)*self.pi)

H=int(input())
P=3.14

p=Cir(H,P)
result=p.cla()
print(f"{result:.2f}"

# 2. ------------------------
def getCircle_area(r):
    return r * r * 3.14

r = float(input())
area = getCircle_area(r)
print(f"{area:.2f}")

# 1. ------------------------
                # lth = r
def get_area_circle(lth):
    area = lth * lth * 3.14
    return area

r = int(input())
print(r)
ret = get_area_circle(r)
# print(ret)
print("%.2f" % ret)