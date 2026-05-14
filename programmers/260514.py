def solution(array):
    array.sort()
    answer = array[len(array)//2]
    return answer

array1 = [1, 2, 7, 10, 11]
array2 = [9, -1, 0]
print(solution(array1))
print(solution(array2))