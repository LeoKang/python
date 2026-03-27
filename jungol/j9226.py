# 6. ----------------------------
a, b = map(int, input().split())
if a > b:
    print(b ,a, sep = '\n')
else:
    print(a, b, sep = '\n')

# 5. ----------------------------------
a, b = map(int, input().split())
print(min(a, b))
print(max(a, b))

# 4. ----------------------------------
for n in sorted(map(int, input().split())):
    print(n)
# 3. ----------------------------------
a, b = map(int, input(). split())
if a > b:
    a, b = b, a
print(a) 
print(b) 

# 2. --------------------------------
a,b=map(int, input().split())
if (a>b):
    a,b=b,a
    #print(a)
    #print(b)
#else:
    #print(a)
    #print(b)
print(a)
print(b)

# 1. -----------------------------------
a, b = map(int, input().split())

if a < b:
    print(a)
    print(b)
else:
    print(b)
    print(a)
