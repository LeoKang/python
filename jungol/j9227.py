a, b = map(int, input().split())
c = [a,b]

print(max(c))   # = print(max(a, b))

# 1. --------------------------------

a, b = map(int, input().split())
print(a, b)

if a > b:
    print(a)
else:
    print(b)