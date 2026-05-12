def solution(num_list, n):
    return [num_list[i : i + n] for i in range(0, len(num_list), n)]

# 1. -------------------------------

def solution(num_list, n):
    answer = []   
    cnt = 0
    tmp = []
    for i in range(len(num_list)):
        tmp.append(num_list[i])
        cnt+=1

        if cnt==n:
            cnt = 0
            answer.append(tmp.copy())
            tmp.clear()

    return answer

lst1 = [1, 2, 3, 4, 5, 6, 7, 8]
lst2 = [100, 95, 2, 4, 5, 6, 18, 33, 948]

print(solution(lst2, 3))