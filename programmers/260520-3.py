def solution(cipher, code):
    answer = []
    for idx, char in enumerate(cipher):
        if (idx + 1) % code == 0:
            answer.append(char)
            
    return "".join(answer)

# 3. -------------------------

def solution(cipher, code):
    len2 = len(cipher)//code + 1
    return "".join(cipher[i*code-1] for i in range(1, len2)) 

# 2. -------------------------

# def solution(cipher, code):
#     return cipher[code-1::code]

# 1. ------------------------

# def solution(cipher, code):
#     answer = ''
#     cnt = 0
#     for c in cipher:
#         cnt+=1
#         if cnt % code == 0:
#             answer += c

#     return answer

cipher1 = "dfjardstddetckdaccccdegk"
code1 = 4
cipher2 = "pfqallllabwaoclk"
code2 = 2
print(solution(cipher1, code1))
# print(solution(cipher2, code2))