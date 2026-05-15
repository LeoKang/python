def solution(my_strings, parts):
    answer = []
    for idx, string in enumerate(my_strings):
        s, e = parts[idx]
        answer.append(string[s : e + 1])
        
    return "".join(answer)

# 1. ---------------------------------------

def solution(my_strings, parts):
    answer = ''
    for i in range(len(my_strings)):
        answer += my_strings[i][int(parts[i][0]):int(parts[i][1]+1)]

    return answer

print(
    solution(
        ["progressive", "hamburger", "hammer", "ahocorasick"],
        [[0, 4], [1, 2], [3, 5], [7, 7]]))