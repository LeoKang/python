N = int(input())
# print(N)
stars = "*" * N

for i in range(N):
    print(stars[:N - i])
# 2. -----------------------
n = int(input())
for i in range(n,0,-1):
    print('*'*i)

# 1. ------------------------
N = int(input())
# print(N)

for x in range(N):
    for y in range(0, N-x):
        print("*", end="")
    print()