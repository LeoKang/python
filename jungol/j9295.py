S, E = map(int,input().split())
# print(S, E)
print(*range(S, E + 1), sep='   ')

# 2. ---------------------------------
S,E=map(int,input().split())

for i in range(S,E+1):
    print(i,end="   ")
# 1. ----------------------------------
S, E = map(int, input().split())
# print(S, E)

for x in range(S, E+1):
    print(x, "  ", end='')
