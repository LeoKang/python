sum(str(x).count(str(k)) for x in range(i, j + 1))

# 1. ----------------------------
def solution(i, j, k):
    st = ""
    for n in range(i, j+1):
        st += str(n)

    answer = 0
    for i in st:
        if int(i)==k:
            answer+=1

    return answer

i = 1
j = 13
k = 1

print(solution(i, j, k))

i = 10
j = 50
k = 5

print(solution(i, j, k))