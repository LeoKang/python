n, m = map(int, input().split())
# print(n, m)
for i in range(1, n * m + 1):
    print(i, end=" ")
    if i % m == 0:
        print()

# 1. -------------------------------

n, m = map(int, input().split())
print(n, m)

num = 1
for row in range(n):
    for col in range(m):
        print(num, end=" ")
        num += 1
    print()