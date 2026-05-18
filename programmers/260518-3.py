def solution(s):
    return ''.join(sorted(c for c in set(s) if s.count(c) == 1))

# 2. --------------------------

def solution(s):
    char_counts = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1
        
    result = []
    for char, count in char_counts.items():
        if count == 1:
            result.append(char)
            
    result.sort()
    return "".join(result)

# 1. --------------------------

# def solution(p):
#     answer = ""
#     s = set(p)

#     for c in s:
#         if p.count(c) == 1:
#             answer += c
    
#     str1 = list(answer)
#     str1.sort()
    
#     answer = ""
#     for c in str1:
#         answer += c

#     return answer

inp1 = "abcabcadc"
inp2 = "abdc"

print(solution(inp1))
print(solution(inp2))