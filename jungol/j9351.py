my_list = []
for _ in range(30):
    num = int(input())
    my_list.append(num)
    
print(*my_list)
# 2. ------------------------
numbers = [int(input()) for _ in range(30)]
print(*numbers)
# 1. ------------------------
lst = []

for i in range(5):
    lst.append(int(input()))

print("-----")
for i in lst:
    print(i, end=' ')