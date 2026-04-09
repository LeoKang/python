A = ['a', 'b', 'c', 'd', 'e']

print(A)
i = len(A) - 1

while i >= 0:
    print(A[i], end=' ')
    i -= 1
# 1. ---------------------------------
A = ['a','b','c','d','e']
print(A)

for x in A:
    print(x, end=' ')
print()

for x in range(len(A)-1, -1, -1):
    print(A[x], end=' ')
print()

length = len(A)
# print(length)

i = 1
while i <= length:
    print(A[length-i], end=' ')
    i+=1
