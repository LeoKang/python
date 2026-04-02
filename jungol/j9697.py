class Player:
    def __init__(self, name, ab, hit):
        self.name = name
        self.ab = ab
        self.hit = hit

    def avg(self): 
        return self.hit / self.ab

    def show(self): 
        print(f"name:{self.name}, AVG:{self.avg():.3f}, AB:{self.ab}, H:{self.hit}")


name1, ab1, hit1 = input().split()
name2, ab2, hit2 = input().split()

p1 = Player(name1, int(ab1), int(hit1))
p2 = Player(name2, int(ab2), int(hit2))

p1.show()
p2.show()
# 4. ------------------------------------
class Baseball:
    def __init__(self, name, ab, h):
        self.name = name
        self.ab = int(ab)
        self.h = int(h)

team = []
for _ in range(2):
    name, ab, h = input().split()
    team.append(Baseball(name, ab, h))
    # print(name, ab, h)

for member in team:
    raw_avg = member.h / member.ab
    rounded_avg = round(raw_avg, 3)
    
    res = f"name:{member.name}, AVG:{rounded_avg:.3f}, AB:{member.ab}, H:{member.h}"
    print(res)
# 3. ----------------------------------------------
class baseball:
    def __init__(self, name, tasu, ang):
        self.name = name
        self.tasu = tasu
        self.ang = ang
    def like(self):
        print(f'name:{self.name}, AVG:{self.ang / self.tasu:.3f}, AB:{self.tasu}, H:{self.ang}')

name, tasu, ang = input().split()
name2, tasu2, ang2 = input().split()


b1 = baseball(name, int(tasu), int(ang))
b2 = baseball(name2, int(tasu2), int(ang2))

b1.like()
b2.like()
# 2. ----------------------------------------------
class Player():
    def __init__(self, name, AB, H):
        self.name = name
        self.AB = AB
        self.H = H
    def avg(self):
        return round(self.H / self.AB, 3)
    def profile(self):
        return f"name:{self.name}, AVG:{self.avg()}, AB:{self.AB}, H:{self.H}"

players = []

for _ in range(2):
    A, B, C = input().split()
    players.append(Player(A, int(B), int(C)))

for i in players:
    print(i.profile())
# 1. -----------------------------------------
class Player:
    def __init__(self, name, ab, h):
        self.name = name
        self.ab = ab
        self.h = h

    def print(self):
        print(f"name:{self.name}, AVG:{self.getAVG()}, AB:{self.ab}, H:{self.h}")
        print(format(self.getAVG(), ".3f"))

    def getAVG(self):
        return int(self.h)/int(self.ab)

for i in range(2):
    name, ab, h = input().split()
    print(name, ab, h)
    p = Player(name, ab, h)
    p.print()
