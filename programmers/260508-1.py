def solution(num_str):
    answer = sum([int(char) for char in num_str])
    return answer

# 1. -----------------------

def solution(num_str):
    answer = 0

    for i in num_str:
        answer += int(i)

    return answer

num_str1 = "123456789"
num_str2 = "1000000"

print(solution(num_str1))
print(solution(num_str2))