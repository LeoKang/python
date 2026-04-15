S = int(input())
E = int(input())
# print(S, E)
step = 1
if S < E:
    step = 1
else:
    step = -1

for i in range(1, 10):
    for j in range(S, E+step, step):
        print(f"{j} * {i} = {i * j}   ", end='')
    print()
