def solution(n):
    answer = []
    
    x = 2
    while x <= n:
        if n % x == 0:
            if x not in answer:
                answer.append(x)
            n //= x
        else:
            x += 1
    return answer

# 2. -------------------------------

def solution(n):
    answer = []
    i = 2
    while i <= n:
        while n % i == 0:
            answer.append(i) 
            n //= i
        i += 1
        
    return sorted(list(set(answer)))

# 1. ---------------------------

# def solution(n):
#     answer = []

#     while True:
#         for i in range(2, n+1):
#             if n % i == 0:
#                 answer.append(i)
#                 n = n / i
#                 i = 2
#                 continue
#         break

#     return answer

n1 = 12
n2 = 17
n3 = 420
n4 = 3

print(solution(n1))
print(solution(n2))
print(solution(n3))
print(solution(n4))