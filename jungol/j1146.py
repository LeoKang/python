n = int(input())
arr = list(map(int, input().split()))

for i in range(n - 1):              
    min_idx = i  

    for j in range(i + 1, n):  
        if arr[j] < arr[min_idx]: 
            min_idx = j

    arr[i], arr[min_idx] = arr[min_idx], arr[i]

    print(*arr)
    
# 3. --------------------------------------------
N = int(input())
nums = list(map(int, input().split()))

for i in range(N - 1):
    min_idx = i

    for j in range(i + 1, N):
        if nums[j] < nums[min_idx]:
            min_idx = j

    nums[i], nums[min_idx] = nums[min_idx], nums[i]
    print(*nums)

# 2. -----------------------------------------
n=int(input())
l=list(map(int,input().split()))
for i in range(len(l)-1):
    m=l[i:].index(min(l[i:]))+i
    l[m],l[i] = l[i],l[m]
    print(*l)

# 1. ----------------------------------------
N = int(input())
# print(N)
inp = list(map(int, input().split()))
# print(*inp)

for j in range(N-1):
    min = inp[j]
    idx = j
    for i in range(j, N):
        if min > inp[i]:
            min = inp[i]
            idx = i
    
    # print(min, i)
    inp[j], inp[idx] = min, inp[j]

    for i in inp:
        print(i, end=" ")
    print()