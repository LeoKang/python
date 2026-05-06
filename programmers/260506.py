# 프로그래머스-코딩테스트 연습-코딩 기초 트레이닝-정수 찾기

def solution(num_list, n):
    answer = 0
    answer = 1 if num_list.count(n) > 0 else 0
    return answer

# 1. --------------------------------
def solution(num_list, n):
    # print(num_list, n)
    answer = 0
    for i in num_list:
        if i == n:
            answer = 1
            break;

    return answer

lst1 = [1, 2, 3, 4, 5]
lst2 = [15, 98, 23, 2, 15]

print(solution(lst2, 20))