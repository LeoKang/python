N = int(input())
# print(N)

# 4. ---------------------------
def print_tens(N):
    i = 10
    while i <= N:
        print(i)
        i += 10

limit = int(input())
# print(limit)
print_tens(limit)

# 3. ---------------------------
N = int(input())
for i in range(10,N+1,10):
    print(i)

# 2. - while -------------------
j = 10
while j<=N:
    print(j)
    j += 10

# 1. - for ---------------------
# for i in range(10, N+1):
#     if i%10 == 0:
#         print(i)
