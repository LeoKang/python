def mul(a, b, c):
    for i in range(1, 10):
        print(f"{a} * {i} = {a * i}   {b} * {i} = {b * i}   {c} * {i} = {c * i}")
  
mul(5, 6, 7)
# 2. ---------------------------
i = 1
while i <= 9:
    j = 5
    while j <= 7:
        res = f"{j} * {i} = {j * i}"
        print(res, end="")
        
        if j < 7:
            print("   ", end="")
        
        j += 1
    print()
    i += 1
# 1. ----------------------------
for i in range(1, 10):
    for j in range(5, 8):
        print(f"{j} * {i} = {i*j}   ", end='')
    print()