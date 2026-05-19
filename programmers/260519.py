def solution(order):
    return sum(1 for c in str(order) if c in '369')

# 2. -------------------------

def solution(order):
    answer = 0
    while order > 0:
        digit = order % 10
        if digit == 3 or digit == 6 or digit == 9:
            answer += 1
        order //= 10
        
    return answer

# 1. ------------------------

def solution(order):
    answer = 0
    for n in str(order):
        if int(n) % 3 == 0 and int(n) != 0:
            answer += 1
    
    return answer

order1 = 3
order2 = 29423
order3 = 0
# print(solution(order1))
# print(solution(order2))
print(solution(order3))