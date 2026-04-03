N = int(input())
# print(N)
for i in range(5, N + 1):
    if i & 1:
        print(i)
# 2. --------------------------
N = input()

start = 5
while start <= int(N):
    print(start)
    start = start + 2 # start += 2

# 1. --------------------------
# N = input()
# # print(N)

# for i in range(5, int(N)+1, 2):
#     print(i)