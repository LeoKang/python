def ElonMusk(x, a, b, c):
    return a * (x**2) + b * x + c

a, b, c = map(int, input().split())
# print(a, b, c)
for x in [2, 3, 5]:
    print(ElonMusk(x, a, b, c))
    
# 1 . -----------------------------------
a, b, c = map(int, input().split())
# print(a, b, c)

def func(x, a, b, c):
    res = a * x * x + b * x + c
    return res

print(func(2, a, b, c))
print(func(3, a, b, c))
print(func(5, a, b, c))