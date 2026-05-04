def get_min_max(arr, low, high):
    if low == high:
        return arr[low], arr[low]
    
    if high == low + 1:
        return (max(arr[low], arr[high]), min(arr[low], arr[high]))
    
    mid = (low + high) // 2
    max1, min1 = get_min_max(arr, low, mid)
    max2, min2 = get_min_max(arr, mid + 1, high)
    
    return max(max1, max2), min(min1, min2)

max_val, min_val = get_min_max(nums, 0, len(nums) - 1)
result = max_val - min_val

# 2. --------------------------------
TC = int(input())

for i in range(1, TC + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    print(f'#{i} {max(nums) - min(nums)}')

# 1. --------------------------------
T = int(input())
for t in range(T):
    N = int(input())
    inp = list(map(int, input().split()))
    # print(*inp)

    min = 1000001
    for i in range(N):
        if min > inp[i]:
            min = inp[i]  
    # print(min)

    max = 0
    for i in range(N):
        if max < inp[i]:
            max = inp[i] 
    # print(max)
    print(f"#{t+1} {max-min}")
