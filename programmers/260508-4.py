def solution(age):
    answer = ''
    for digit in str(age):
        answer += chr(ord('a') + int(digit))
        
    return answer 

# 2. ------------------------------

def solution(age):
    return "".join(["abcdefghij"[int(i)] for i in str(age)])

# 1. -----------------------------

def solution(age):
    answer = ''
    s = str(age)
    for i in s:
        answer += chr(ord('a') + int(i))

    return answer

age1 = 23
age2 = 51

print(solution(age2))