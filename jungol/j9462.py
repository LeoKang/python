def bubble_sort(arr, n, current_pass=1):
    if current_pass == n:
        return
    
    for x in range(len(arr) - current_pass):
        if arr[x] > arr[x + 1]:
            arr[x], arr[x + 1] = arr[x + 1], arr[x]
            
    print(arr)
    bubble_sort(arr, n, current_pass + 1)

N = int(input())
nums = list(map(int, input().split()))

bubble_sort(nums, N)

# 2. --------------------------------

N=int(input())

hap=list(map(int,input().split()))

for i in range(N-1):
    for j in range(1,N-i):
        if hap[j-1] > hap[j] :
            hap[j-1], hap[j] = hap[j], hap[j-1]
    print(hap)

# 1. --------------------------------

#bubble sort
N = int(input())
lst = list(map(int, input().split()))

# print(lst)
isSorted = True

while isSorted:
    isSorted = False
    for i in range(len(lst)-1):
        if lst[i]>lst[i+1]:
            tmp = lst[i]
            lst[i] = lst[i+1]
            lst[i+1] = tmp
            isSorted = True
    if isSorted == True:
        print(lst)