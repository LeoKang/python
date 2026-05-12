#프로그래머스-코딩테스트연습-코딩테스트-입문-짝수홀수개수

def solution(num_list):

    answer = [0, 0]
    for n in num_list:
        answer[n % 2] += 1

    return answer

# 1. -----------------------

def solution(num_list):
    answer = []

    print(num_list)

    odd = 0
    even = 0
    for i in num_list:
        print(i)
        if i%2==0:
            even+=1
        else:
            odd+=1

    print(odd, even)
    answer = [even, odd] 
    print(answer)

    return answer

p1 = [1, 2, 3, 4, 5]
p2 = [1, 3, 5, 7]
                    # [짝수의 개수, 홀수의 개수]
print(solution(p1)) # ret : [2, 3]
print(solution(p2))