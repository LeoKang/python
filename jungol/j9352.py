list1=list(map(int, [input() for _ in range(50)]))
for i in reversed(list1):
    print(i,end=" ")
# 3. --------------------------
inp = [int(input()) for i in range(50)]
# print(inp)
print(*inp[::-1])

# 2. -------------------------
L =[]
for i in range(50):
    L.append(int(input()))
print(*L[::-1])

# 1. ------------------------
inp = []

for i in range(50):
    x = input()
    inp.append(x)

for x in range(len(inp)-1, -1, -1):
    print(inp[x], end=' ')