dict = {1:"one", 2:"two", 3:"three"}
while True:
    inp = int(input())
    # print(inp)
    if inp in dict:
        print(dict[inp])
    else:
        break
# 3. -------------------------
while True:
    n = int(input())
    match n:
        case 1: print("one")
        case 2: print("two")
        case 3: print("three")
        case _: break
# 2. -----------------------
def f(n):
    if n==1: return "one"
    if n==2: return "two"
    if n==3: return "three"
    return None

while True:
    v=int(input())

    if v < 1 or v >3 :
        break
    print(f(v))

# 1. -----------------------
while True:
    num = int(input())
    if num == 1:
        print("one")
    elif num == 2:
        print("two")
    elif num == 3:
        print("three")
    else:
        break
