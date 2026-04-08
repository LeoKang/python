a='apple orange banana'
b='   Hello world!   '

print(' '.join(reversed(a.split())))
print(b)
print(b.strip())
# 5. -------------------------------

A = "apple orange banana"
B = "   Hello world!   "
A = "banana orange apple"
print(A)
print(B)
print(B.strip())

# 4. -------------------------------

A=["apple" , "orange" , "banana"]
B='   "Hello world!"   '
print(*A[::-1])
print(B.replace('"', ""))
print(B.replace('"', "").strip())
# 3. ----------------------------
a = "apple orange banana"
b = "   Hello world!   "

words = a.split()
print(' '.join(words[::-1]))
print(b)
print(b.strip())
# 2. -----------------------------
A = "apple orange banana"
words = A.split()[::-1]
print(*words)

B = "   Hello world!   "
print(B)
print(B.strip())

# 1. ----------------------------
A = "apple orange banana"
B = "   Hello world!   "

retA = A.split()
# print(retA)

idx = len(retA)
# print(idx)

for x in range(idx-1, -1, -1):
    print(retA[x], end=' ')
print()
print(B)
print(B.strip())