S, E, K = [int(input()) for _ in range(3)]

print(*range(S, E + 1, K), sep='\n')

# 1. --------------------
S = int(input())
E = int(input())
K = int(input())
# print(S, E, K)

for x in range(S, E+1, K):
    print(x)