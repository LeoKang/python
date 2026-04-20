nums = [int(input()) for i in range(5)]
print(nums)
print(*nums)
# 1. ---------------------
lst = []
for i in range(5):
    inp = int(input())
    lst.append(inp)

print(lst)
for i in lst:
    print(i, end=' ')