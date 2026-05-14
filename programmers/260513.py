def solution(my_string):
    char_dict = {}
    for char in my_string:
        char_dict[char] = 0
    
    return "".join(char_dict.keys())

# 1. --------------------------

# def solution(my_string):
#     lst = []
#     s = set()

#     for i in my_string:
#         if i not in s:
#             s.add(i)
#             lst.append(i)

#     answer = ''.join(lst)
#     return answer

my_string1 = "people"
my_string2 = "We are the world"
print(solution(my_string1))
print(solution(my_string2))