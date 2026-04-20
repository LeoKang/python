nums = [1, 2, 3, 4, 5]  # 1번

last_val = nums.pop()
print(f"last: {last_val}")  # 2번

print(nums)
print(f"len: {len(nums)}")  # 3번

second_val = nums.pop(1)
print(f"second: {second_val}")  # 4번

print(nums)
print(f"len: {len(nums)}")  # 5번
# 1. -------------------------
lst = [1, 2, 3, 4, 5]
print(f"last: {lst[-1]}")
lst.remove(lst[-1])
print(lst)
print(f"len: {len(lst)}")

print(f"second: {lst[1]}")
lst.remove(lst[1])
print(lst)
print(f"len: {len(lst)}")