def solution(my_str, n):
    return [my_str[i : i + n] for i in range(0, len(my_str), n)]

# 2. ----------------------------

def solution (my_str,n):
    m=[]
    while len(my_str)!=0:
        m.append(my_str[:n])
        my_str=my_str[n:]
    return m

# 1. -------------------------------
def solution(my_str, n):
    answer = []
    str = ""
    i = 0
    for j in my_str:
        str += j
        i+=1
        if i % n == 0:
            answer.append(str)
            str = ""

    if str != "":
        answer.append(str)

    return answer

my_str1 = "abc1Addfggg4556b"
n1 = 6

my_str2 = "abcdef123"
n2 = 3

print(solution(my_str1, n1))
print(solution(my_str2, n2))