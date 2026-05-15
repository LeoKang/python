def solution(array, n):
    array.sort()

    arr = []

    for i in range(len(array)):
        arr.append(abs(array[i] - n))

    return array[arr.index(min(arr))]

# 2. --------------------------------

def solution(array, n):

    temp = []
    for x in array:
        temp.append([abs(x - n), x])

    temp.sort()

    return temp[0][1]

# 1. --------------------------------

# def solution(array, n):
#     array.append(n)
#     array.append(-100)
#     array.append(201)
#     array.sort()
#     idx = array.index(n)

#     dist1 = array[idx] - array[idx-1]
#     dist2 = array[idx+1] - array[idx]

#     if dist1 < dist2:
#         answer = array[idx-1]
#     elif dist1 == dist2:
#         answer = array[idx-1]
#     else:
#         answer = array[idx+1]

#     return answer

array1 = [3, 10, 28]
n1 = 20

array2 = [10, 11, 12]
n2 = 13

print("ret : ", solution(array1, n1))
print("ret : ", solution(array2, n2))