def solution(n):
    answer = (n - 1) // 7 + 1
    return answer

# 3. ------------------------------

import math

def solution(n):
    return math.ceil(n / 7)
    return math.celi(n / 7)

# 2. -----------------------------

function solution(n) {
    if (n%7 !==0) {
        a = Math.trunc(n / 7) +1
    }else{
        a = Math.trunc(n / 7)
    }
    return a;
}


# 1. --------------------------------------

def solution(n):
    if n<=7:
        return 1
    else:
        rest = 0

        n = n // 7
        if n% 7 != 0:
            rest = 1
        else:
            rest = 0

    answer = n + rest
    return answer

n1 = 7
n2 = 15
print(solution(n1))
print(solution(n2))