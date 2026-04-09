a, b = map(int, input().split())

first = a % 2
second = b + 10
total = first + second

print(first, second, total)
# 3. --------------------------------
a, b = map(int, input().split())
res = [a % 2, b + 10]
print(*(res + [sum(res)]))
# 2. --------------------------------
def cal(N, M):
    A = N%2
    B = M+10
    return A, B, A+B

N, M = map(int, input().split())
a, b, c = cal(N, M)
print(*cal(N, M))

# 1. ---------------------------------
a, b = map(int, input().split())
# print(a, b)

a = a % 2 # a %= 2
b += 10
print(a, b, (a+b))