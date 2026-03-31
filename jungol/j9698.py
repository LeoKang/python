class N:
    def __init__(self, year, price):   
        self.year = year
        self.price = price

    def check(self, Y, P): 
        return self.year >= Y and self.price <= P

N_num = int(input())

buildings = []

for _ in range(N_num):
    year, price = map(int, input().split())
    buildings.append(N(year, price))

Y, P = map(int, input().split())

for b in buildings:
    if b.check(Y, P):
        print(b.year, b.price)

# 3. ----------------------------------------
class Building:
    def __init__(self, year, price):
        self.year = year
        self.price = price

n = int(input())

delpi = [Building(*map(int, input().split())) for _ in range(n)]

target_y, target_p = map(int, input().split())

for b in delpi:
    if b.year >= target_y and b.price <= target_p:
        print(b.year, b.price)

# 2. --------------------------------
class Z:
    def __init__(self):
        self.hap=[]
        self.hap1=[]

    def X(self,n):
        for i in range(n):
            a,b=map(int, input().split())
            self.hap.append((a,b))

        c,d=map(int, input().split())

        for i in range(n):
            if self.hap[i][0]>=c and self.hap[i][1]<=d :
                self.hap1.append(self.hap[i])
        
        for i in self.hap1:
            print(i[0],i[1])

n = int(input())
J = Z()
J.X(n)
# 1. -----------------------------------
class Building:
    def __init__(self, year, price):
        self.year = year
        self.price = price
    def print_building(self):
        print(self.year, self.price)

blst = []

N = int(input())
for i in range(N):
    year, price = map(int, input().split())
    b = Building(year, price)
    blst.append(b)

Y, P = map(int, input().split())

for k in range(N):
    if blst[k].year >= Y and blst[k].price <= P:
        blst[k].print_building()