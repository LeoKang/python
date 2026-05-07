function solution(array, height) {
    return array.filter(v => v > height).length;
}

# 2. -------------------------
def solution(array, height):
    array.append(height)
    array.sort(reverse=True)
    return array.index(height)

# 1. -----------------------
def solution(array, height):
    array.sort()
    cnt = 0
    for i in array:
        if i <= height:
            cnt += 1

    return len(array)-cnt

array1 = [149, 180, 192, 170]
height1 = 167
array2 = [180, 120, 140]
height2 = 190

print(solution(array1, height1))
print(solution(array2, height2))