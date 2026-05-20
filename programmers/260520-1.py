def fac(num):
    a = 1
    for i in range(1, num + 1):
        a *= i
    return a

def solution(balls, share):
    
    n = fac(balls)
    m = fac(share)
    nm = fac(balls - share)

    return n / nm * m

# 2. -------------------------

def solution(balls, share):
    answer = 1
    temp = 1

    for x in range(balls, balls-share, -1):
        answer *= x

    for y in range(share, 0, -1):
        temp *= y

    return answer // temp

# 1. --------------------------

b = []
share = 0
balls = 0

def init(balls, share):
    for i in range(balls):
        b.append(0)

    global gshare
    gshare = share
    global gballs
    gballs = balls
    print(b)
    print(gshare)

def plus(n):
    if n == gballs:
        cnt = 0
        for i in b:
            if i==1:
                cnt += 1
        
        if cnt == gshare:
            for i in b:
                print(i, end=' ')
            print()
        
        return

    for i in range(0, 2):
        b[n] = i
        plus(n+1)

def solution(balls, share):
    init(balls, share)

    plus(0)

    answer = 0
    return answer

# import math
# def solution(balls, share):
#     answer = 0

#     t = math.factorial(balls)
#     b1 = math.factorial(balls-share)
#     b2 = math.factorial(share)

#     answer = int(t / (b1 * b2))

#     return answer

balls1 = 3
share1 = 2
balls2 = 5
share2 = 3
print(solution(balls2, share2))