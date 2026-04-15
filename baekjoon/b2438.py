n = int(input())

i = 1
while i <= n:
    print("*" * i)
    i += 1
# 3. -------------------------
def print_stars(limit, current):
    if current > limit:
        return
    
    print('*' * current)
    print_stars(limit, current + 1)

n = int(input())
# print(n)
print_stars(n, 1)

# 2. -------------------------
N = int(input())
for i in range(1, N+1):
    print('*'*i)

# 1. -------------------------
N = int(input())
print(N)

for i in range(N):
    for j in range(N):
        if i>=j:
            print("*", end='')
    print()