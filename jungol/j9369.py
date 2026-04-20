ist = []

while True:
    n = int(input())
    if n == -1:
        break
    list.append(n)

print(*list[-3:])

#-------------------

list = []
for i in range(n):
    n = int(input())
    if n == -1:
        break
    list.append(n)

print(*list[-3:])
#2. ------------------------------
A = []

for val in iter(input, "-1"):
    A.append(int(val))

print(*A[-3:])

#1. -------------------------------
inp = 0
lst = []
while True:
    inp = int(input())
    # print(inp)
    if inp == -1:
        break
    if len(lst) == 3:
        lst.pop(0)
    lst.append(inp)

print(*lst)