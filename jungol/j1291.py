while True:
    s, e = map(int, input().split())

    if 2 <= s <= 9 and 2 <= e <= 9:
        break
    else:
        print("INPUT ERROR!")

step = 1 if s <= e else -1

for i in range(1, 10):
    row = []
    for dan in range(s, e + step, step):
        row.append(f"{dan} * {i} = {dan * i:2d}")
    print("   ".join(row))
# 2. ------------------------------------
while True:
    a, b = map(int, input().split())
    if 2 <= a <= 9 and 2 <= b <= 9:
        step = 1 if a <= b else -1
        gugudan = range(a, b + step, step)
        
        for i in range(1, 10):
            line = [f"{nums} * {i} = {nums * i:2d}" for nums in gugudan]
            print("   ".join(line))
        break
    else:
        print("INPUT ERROR!")
# 1. ------------------------------------
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