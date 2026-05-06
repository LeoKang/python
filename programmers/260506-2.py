# 프로그래머스-코딩테스트 연습-코딩테스트 입문-배열 두 배 만들기

def solution(numbers):
    answer = []
    for n in numbers:
        answer.append(n << 1)
    return answer

# 1. --------------------------

def solution(numbers):
    answer = []
    for i in numbers:
        answer.append(i * 2)
    return answer

lst1 = [1, 2, 3, 4, 5]
lst2 = [1, 2, 100, -99, 1, 2, 3]
print(solution(lst2))