def solution(array):
    count = {}
    for num in array:
        count[num] = count.get(num, 0) + 1
    
    max_count = max(count.values())
    candidates = [num for num, cnt in count.items() if cnt == max_count]
    
    return candidates[0] if len(candidates) == 1 else -1

# 3. ----------------------------

def solution(array):
    nums = 0
    max_val = 0
    for i in set(array):
        if array.count(i) > nums:
            nums = array.count(i)
            max_val = i
        elif array.count(i) == nums:
            max_val = -1
    return max_val

# 2. -----------------------------

def solution(array):
    l=[array.count(x) for x in array]
    if len(l) != 1 and l.count(max(l)) > max(l):
        return -1
    else:
        return array[l.index(max(l))]

# 1. ---------------------------

def solution(array):
    array.sort()
    d = {}
    for i in array:
        if i in d:
            cur = d[i]
            d[i] = cur + 1
        else:
            d[i] = 1
 
    max = -1
    idx = -1
    for k, v in d.items():
        if max < v:
            max = v
            idx = k

    cnt = 0
    for k, v in d.items():
        if v == max:
            cnt+= 1

    if cnt == 1:
        return max
    else:
        return -1

array1 = [1, 2, 3, 3, 3, 4] # ret : 3
print(solution(array1))

array2 = [1] # -1
print(solution(array2))