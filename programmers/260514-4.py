def solution(myString):
    return sorted(myString.replace('x', ' ').split())

# 1. -----------------

def solution(myString):
    answer = []
    st = ""

    for c in myString:
        if c!="x":
            st += c
        else:
            if len(st) != 0:
                answer.append(st)
                st = ""
    
    if len(st) != 0:
        answer.append(st)

    answer.sort()

    return answer

myString1 = "axbxcxdx"
myString2 = "dxccxbbbxaaaa"
myString3 = "xdxccxbbbxaaaa"
# print(solution(myString1))
# print(solution(myString2))
print(solution(myString3))