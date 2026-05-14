def solution(n):
    f = 1
    for i in range(1, 12):
        f *= i
        if f > n:
            return i - 1
        if f == n:
            return i
    return 10 

# 2. -------------------------------

import math
def solution(n):
    t=1
    while n>=math.factorial(t):
        t+=1
    return t-1

# 1. -------------------------------

lst = [1, ]

def solution(n):
    i = 1
    while lst[i-1]<=n:
        lst.append((len(lst)+1) * lst[i-1])
        i+=1

    print(lst)

    return i-1

n1 = 7
n2 = 3628800
print(solution(n2))