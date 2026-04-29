# 프로그래머스-코딩테스트연습-완전탐색-모의고사

import itertools
def solution(answers):
    count1 = itertools.cycle([1,2,3,4,5])
    count2 = itertools.cycle([2,1,2,3,2,4,2,5])
    count3 = itertools.cycle([3,3,1,1,2,2,4,4,5,5])

    Ii=0
    Jj=0
    Kk=0

    for a,b in zip(answers,count1):
        if a == b:
            Ii+=1
    for c,d in zip(answers,count2):
        if c == d:
            Jj+=1
    for e,f in zip(answers,count3):
        if e == f:
            Kk+=1
    list1 = [Ii,Jj,Kk]
    hap = max(list1)
    result = []

    if list1[0] == hap:
        result.append(1)
    if list1[1] == hap:
        result.append(2)
    if list1[2] == hap:
        result.append(3)
    
    return result

# 2. ------------------------------------
def solution(answers):
    m = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    s = [[b[i % len(b)] - a for i, a in enumerate(answers)].count(0) for j, b in enumerate(m)]
    return [i + 1 for i, a in enumerate(s) if a >= max(s)]

# 1. ---------------------------------
ans = [1, 2, 3, 4, 5]   # testcase 1
# ans = [1, 3, 2, 4, 2]   # testcase 2

def solution(answers):
    # print(answers)
    # print(len(answers))

    sp1 = [1, 2, 3, 4, 5]
    sp2 = [2, 1, 2, 3, 2, 4, 2, 5]
    sp3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    score1 = 0
    score2 = 0
    score3 = 0

    for i in range(len(answers)):
        if answers[i] == sp1[i % len(sp1)]:
            score1 += 1
        if answers[i] == sp2[i % len(sp2)]:
            score2 += 1
        if answers[i] == sp3[i % len(sp3)]:
            score3 += 1

    print(score1, score2, score3)
    maxScore = max(score1, score2, score3)
    answer = []
    if maxScore == score1:
        answer.append(1)
    if maxScore == score2:
        answer.append(2)
    if maxScore == score3:
        answer.append(3)

    return answer

res = solution(ans)
print(res)