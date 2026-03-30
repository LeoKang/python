X = int(input())
N = int(input())
c = []
for i in range(N):
    a, b = map(int, input().split())
    c.append(a * b)

if X == sum(c):
    print("Yes")
else:
    print("No")
# 2. -----------------------------------
X=int(input())
A=[]
B=[]
total = 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    
for t in range(len(A)):
    total += A[t] * B[t]

if X==total:
    print('yes')
else:
    print('no')
# 1.------------------------------------
X = int(input())
print(X)
N = int(input())
print(N)
prod = 0
for i in range(N):
    a, b = map(int, input().split())
    print(a, b)
    prod += (a * b)

print(prod)

if X == prod:
    print("Yes")
else:
    print("No")





# 1. --------------------------------------
# X = int(input())
# N = int(input())
# # print(X, N)
# res = 0
# for i in range(N):
#     a, b = map(int, input().split())
#     # print(a, b)
#     res += a * b

# if X==res:
#     print("Yes")
# else:
#     print("No")
