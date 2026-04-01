class Soccer:
    def __init__(self,T,W):
        self.T=T
        self.W=W
    def WIN_TEAM(self,i):
        if i.win >= self.W :
            return i.team
        return None

T,W=map(int, input().split())
info=Soccer(T,W)

teams=[]

for _ in range(info.T):
    t_name,t_win=input().split()
    teams.append(Soccer(t_name,int(t_win)))

for i in range(info.T -1,-1,-1):
    result = info.WIN_TEAM(teams[i])
    if result:
        print(result)
        
# 3. ---------------------------------
#9699
N, M = map(int,input().split())
L = []
class Xx:
    def __init__(self, n, s):
        self.n = n
        self.s = s
    def __str__(self):
        return f'{self.n}'
for i in range(N):
    n, s =input().split()
    if int(s) >= M:
        L.append(Xx(n, s))
    else:
        continue
for t in L[::-1]:
    print(t.n)

# 2. ----------------------------------
class SoccerTeam:
    def __init__(self, n, p):
        self.name = n
        self.points = int(p)

n, m = map(int, input().split())

teams = [SoccerTeam(*input().split()) for _ in range(n)]

for t in reversed(teams):
    if t.points >= m:
        print(t.name)

# 1.-------------------------------------
class SoccerTeam:
    def __init__(self, name, wp):
        self.name = name
        self.wp = wp
    def print_info(self):
        print(self.name, self.wp)

N, M = map(int, input().split())
lst = []
res = []
for i in range(N):
    team_name, wp = input().split()
    # print(team_name, wp)
    lst.append(SoccerTeam(team_name, wp))

# for j in range(len(lst)):
#     lst[j].print_info()

for k in range(len(lst)):
    if int(lst[k].wp) >= M:
        res.append(lst[k].name)

# print(res)
for x in range(len(res)-1, -1, -1):
    print(res[x])