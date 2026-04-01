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