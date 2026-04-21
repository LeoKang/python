s = 0
e = 0
while True:
    s, e = map(int, input().split())
    if(not(2<=s and s<=9) or not(2<=e and e<=9)):
        print("INPUT ERROR!")
    else:
        break

if s < e:
    for j in range(1, 10):
        for i in range(s, e+1):
            print(f"{i} * {j} = {i*j:2d}", end="   ")
        print()
else:
    for j in range(1, 10):
        for i in range(s, e-1, -1):
            print(f"{i} * {j} = {i*j:2d}", end="   ")
        print()