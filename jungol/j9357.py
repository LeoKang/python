nums = [int(input()) for x in range(5)]
print(nums)

nums = nums[:-2]

print(nums)
# 1. --------------------------
lst = list()

for i in range(5):
    inp = int(input())
    lst.append(inp)

print(lst)

for i in range(2):
    lst.pop()

print(lst)