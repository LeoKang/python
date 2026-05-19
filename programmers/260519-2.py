def solution(array):
    return array.count(7)

# 2. ----------------------

def solution(array):
    full_str = "".join(map(str, array))
    
    removed_str = full_str.replace('7', '')
    
    return len(full_str) - len(removed_str)

# 1. ---------------------

def solution(array):
    answer = 0
    for n in array:
        for c in str(n):
            if int(c)==7:
                answer+=1

    return answer

array1 = [7, 77, 17]
array2 = [10, 29]
print(solution(array1))
print(solution(array2))