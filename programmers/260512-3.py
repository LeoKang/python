def solution(my_string):
    return ''.join(sorted(my_string.lower()))

# 2. ---------------------------------

def solution(my_string):
    str_list = list(my_string.lower())
    
    n = len(str_list)
    for i in range(n):
        for j in range(n - 1 - i):
            if str_list[j] > str_list[j + 1]:
                str_list[j], str_list[j + 1] = str_list[j + 1], str_list[j]
                
    return "".join(str_list)

# 1. -----------------------------

def solution(my_string):
    r = my_string.lower()
    ret = sorted(r)
    answer = ""
    for i in ret:
        answer += i
    
    return answer

print(solution("Bcad"))
print(solution("heLLo"))
print(solution("Python"))