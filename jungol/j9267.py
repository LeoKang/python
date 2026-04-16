lst = []
N = int(input())
for i in range(1, N+1):
    lst.append(i)
lst2 = list(reversed(lst))
print(*lst2, end = ' ')

# 2. -------------------
N = int(input())
print(N)

while N>=1:
    print(N, end=' ')
    N = N - 1

# 1. -------------------
# for i in range(N, 0, -1):
#     print(i, end=' ')