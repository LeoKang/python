# 3. ---------------------
a=int(input())
b=int(input())

c=a-10
d=b*2

print("{} + {} = {}".format(c,d,c+d))

# 2. ---------------------
a,b=map(int,open(0).read().split())
print(f"{a-10} + {b*2} = {(a-10)+(b*2)}")

# 1. ---------------------
n1 = int(input())
n2 = int(input())
# print(n1, n2)

n1 = n1 - 10
# n1 -= 10

n2 *= 2

# print(n1, '+', n2, '=', n1 + n2)
print(f"{n1} + {n2} = {n1 + n2}")
