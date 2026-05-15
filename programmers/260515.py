function solution(my_string) {
    const numbers = my_string.match(/\d+/g);

    if (!numbers) {
        return 0;
    } else {
        return numbers.reduce((acc, curr) => acc + Number(curr), 0);
    }
}

# 2. --------------------------------

def solution(my_string):
    if not any(c.isdigit() for c in my_string):
        return 0
    
    start = -1
    for i, c in enumerate(my_string):
        if c.isdigit():
            start = i
            break
            
    end = start
    while end < len(my_string) and my_string[end].isdigit():
        end += 1
        
    return int(my_string[start:end]) + solution(my_string[end:])

# 1. ------------------------------

# def solution(my_string):
#     answer = 0
#     tmp_num = 0
#     for c in my_string:
#         if c.isdigit():
#             if tmp_num == 0:
#                 tmp_num = int(c)
#             else:
#                 tmp_num = (tmp_num * 10) + int(c)
#         else:
#             answer += tmp_num
#             tmp_num = 0

#     if tmp_num != 0:
#         answer += tmp_num

#     return answer

my_string1 = "aAb1B2cC34oOp"
# my_string2 = "1a2b3c4d123Z"
# my_string3 = "a1b23"
# my_string4 = "ab10cd20ef"

print(solution(my_string1))
# print(solution(my_string2))
# print(solution(my_string3))
# print(solution(my_string4))