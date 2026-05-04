from fractions import Fraction

def solution(numer1, denom1, numer2, denom2):
    result = Fraction(numer1, denom1) + Fraction(numer2, denom2)
    answer = [result.numerator, result.denominator]
    return answer
# 3. ----------------------------------
def solution(denum1, num1, denum2, num2):
    answer = []    
    a = 0
    b = 0

    a = (denum1 * num2) + (denum2 * num1)
    b = num2 * num1
    for j in range(1, 1000):
        for i in range(1, 1000):
            if (a % i) == 0 and (b % i) == 0:
                a = a / i
                b = b / i
        answer = [a, b]

    return answer
# 2. ---------------------------------------

import math

def solution(numer1, denom1, numer2, denom2):
    numer = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2
    g = math.gcd(numer, denom)
    numer //= g
    denom //= g
    return [numer, denom]

# 1. ---------------------------------------

def solution(numer1, denom1, numer2, denom2):
    answer = []
    pdenom1 = denom1
    numer1 *= denom2
    denom1 *= denom2
    numer2 *= pdenom1
    denom2 *= pdenom1

    resnumer = numer1 + numer2

    print(resnumer, denom1) # 10, 8

    for x in range(denom1, 1, -1):
        if resnumer % x == 0 and denom1 % x == 0:
            resnumer /= x;
            denom1 /= x;

    answer.append(int(resnumer))
    answer.append(int(denom1))
    return answer

# print(solution(1, 2, 3, 4))    # 1/2 + 3/4
print(solution(9, 2, 1, 3))    