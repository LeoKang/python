import random
M = []
for t in range(9):
    M.append(int(input()))
R = random.sample(M, 7) 

while sum(R) != 100:
    R = random.sample(M, 7)
    if sum(R)==100 :
        for T in R:
            print(T)
# 1. --------------------------
lst = []
for x in range(9):
    lst.append(int(input()))

# for i in lst:
#     print(i, end=' ')

# print('\nsum : ', sum(lst))

nsum = sum(lst)
reali = 0
realj = 0

for i in range(9):
    for j in range(9):
        if i==j:
            continue
        nsum -= (int(lst[i]) + int(lst[j]))
        # print(lst[i], lst[j], nsum)
        if nsum == 100:
            reali = i
            realj = j
            break
        nsum += (int(lst[i]) + int(lst[j]))

# print(reali, realj)

for i in range(len(lst)):
    if i==reali or i==realj:
        continue
    print(lst[i])