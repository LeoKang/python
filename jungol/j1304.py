n = int(input())
# print(n)
matrix = [[0] * n for _ in range(n)]

num = 1
for j in range(n):      
    for i in range(n):  
        matrix[i][j] = num
        num += 1

for row in matrix:
    print(*(row))

# 1. --------------------------
n = int(input())
# print(n)

for row in range(1, n+1):
    num = row
    for col in range(n):
        print(num, end=" ")
        num = num + n
    print()