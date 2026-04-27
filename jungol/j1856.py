N,M = map(int, input().split())
EX=N*M
j = 1
for i in range(N):
    for _ in range(M):
        if j>EX:
            break
        print(j,end=" ")
        j+=1
    print()

    Q=[]

    for _ in range(M):
        if j>EX:
            break
        Q.append(j)
        j+=1
        
    Q.reverse()
    print(*Q,end=" ")
    print()
# 3. -----------------------------
n, m = map(int, input().split())

num = 1
for i in range(n):
    row = []

    for j in range(m):
        row.append(num)
        num += 1

    if i % 2 == 0:
        print(*row)
    else:
        print(*row[::-1])
# 2. -------------------------------
n, m = map(int, input().split())
# print(n, m)
current_num = 1
for i in range(n):
    row = []
    if i % 2 == 0:
        for j in range(m):
            row.append(current_num)
            current_num += 1
    else:
        for j in range(m):
            row.insert(0, current_num)
            current_num += 1
    print(*row)

# 1. -------------------------------

n, m = map(int, input().split())
# print(n, m)
num = 1
for i in range(n):
    if i % 2 == 0:
        if i != 0:
            num += m
        for j in range(m):
            print(num, end=' ')
            num += 1
    else:
        num = (num-1) + m
        for j in range(num, num-m, -1):
            print(num, end=' ')
            num -= 1
        num += 1
    print()