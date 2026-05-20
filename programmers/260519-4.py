def solution(s):
    stack = []
    
    for item in s.split():
        if item == "Z":
            stack.pop()
        else:
            stack.append(int(item))
    
    return sum(stack)

# 2. -----------------------------

def solution(s):
    stack = []
    for char in s.split():
        if char == "Z":
            if stack:
                stack.pop()
        else:
            stack.append(int(char))
            
    return sum(stack)

# 1. -----------------------------

def solution(s):
    answer = 0
    lst = s.split()
    for i in range(0, len(lst)):
        if lst[i]=='Z':
            lst[i-1] = 0

    for i in range(0, len(lst)):
        if lst[i]!='Z':
            answer += int(lst[i])

    return answer

s1 = "1 2 Z 3"  # 4
s2 = "10 20 30 40"
print(solution(s1))
print(solution(s2))