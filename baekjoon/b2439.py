a=int(input())
for i in range(1,a+1):
    print((i*"*").rjust(a))
    
# 2. ------------------------------
n = int(input())
# print(n)
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * i)

# 1. ------------------------------
N = int(input())
print(N)

for row in range(N):
    for col in range(N-row-1):
        print("?", end='')
    for col2 in range(row+1):
        print("*", end='')
    print()