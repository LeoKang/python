X = int(input())
N = int(input())
# print(X, N)
res = 0
for i in range(N):
    a, b = map(int, input().split())
    # print(a, b)
    res += a * b

if X==res:
    print("Yes")
else:
    print("No")
