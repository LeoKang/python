N = int(input())
if 1<= N <=9:
    for i in range(1,10):
     print(f"{N} * {i} =",N*i)
# 4. ------------------------------------
N = int(input())
for i in range(1, 10):
    print(f"{N} * {i} = {N * i}")
# 3. ------------------------------------
N = int(input())
for x in range(1, 10, 1):
    print(f'{N} * {x} =', N*x)

# 2. ------------------------------------
N = int(input())
print('\n'.join([f"{N} * {i} = {N * i}" for i in range(1, 10)]))

# 1. -----------------------------------
# N = int(input())
# # print(N)

# for i in range(9):
#     print(N, '*' , i+1, '=', N*(i+1))