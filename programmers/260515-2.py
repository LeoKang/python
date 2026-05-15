def solution(n):
    return [i for i in range(1, n + 1) if i % 2 == 1]

# 1. ------------------------

def solution(n):
    answer = []

    for i in range(1, n+1, 2):
        answer.append(i)

    return answer

n1 = 15

print(solution(n1))