for i in range(1, 6):
    count = abs(i - 3) + 1
    print('*' * count)

# 2. ------------------------

N = 3

for i in range(N):
    for j in range(N-i, 0, -1):
        print("*", end="")
    print()

for i in range(1, N):
    for j in range(i+1):
        print("*", end="")
    print()
