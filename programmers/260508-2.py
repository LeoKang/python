# 프로그래머스-코딩테스트 연습-코딩테스트 입문 - 진료순서 정하기

def solution(emergency):
    answer = []
    sorted_list = sorted(emergency, reverse=True)

    for ch in emergency:
        answer.append(sorted_list.index(ch) + 1)

        return answer

# 4. ------------------------------------

def solution(emergency):
    n = len(emergency)
    answer = [n] * n 
    
    for i in range(n):
        for j in range(n):
            if i == j: continue
            if emergency[i] > emergency[j]:
                answer[i] -= 1
                
    return answer

# 3. ---------------------------

def solution(lst_one):
    answer = []
    for i in lst_one:
        count = 1
        for j in lst_one:
            if j > i:
                count += 1
        answer.append(count)
        
    return answer

# 2. -----------------------------------

def solution(emergency):
    E = sorted(emergency, reverse=True)
    return [E.index(i) + 1 for i in emergency]

# 1. ---------------------------------

def solution(emergency):
    answer = []
    v = []

    for i in emergency:
        v.append(i)
    v.sort()
    reversedv = v[::-1]
    for i in emergency:
        answer.append(reversedv.index(i) + 1)

    return answer

print(solution([3, 76, 24]))
print(solution([1, 2, 3, 4, 5, 6, 7]))
print(solution([30, 10, 23, 6, 100]))