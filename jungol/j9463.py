def bubble_sort(arr, n):
    if n == 1:
        return

    for j in range(len(arr) - (len(arr) - n + 1)):
        if arr[j] < arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    print(*(arr))
    
    bubble_sort(arr, n - 1)

nums = list(map(int, input().split()))
bubble_sort(nums, len(nums))

# 1. ---------------------------------------
lst = list(map(int, input().split()))
# print(lst)

for j in range(len(lst)-1):
    for i in range(len(lst)-1):
        if lst[i]<lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]
    print(*lst)