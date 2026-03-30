a = int(input())

def Number():
    print(f"{a} + 10 = {a+10}")
    print(f"{a} - 10 = {a-10}")

Number()
# 2. ---------------------------------

def solve(n, task):
    if task == 'plus10':
        return f"{n} + 10 = {n + 10}"
    elif task == 'minus10':
        return f"{n} - 10 = {n - 10}"

num = int(input())
print(solve(num, 'plus10'))
print(solve(num, 'minus10'))

# 1. ----------------------------
def func_plus(param):
    return param + 10

def func_minus(param):
    return param - 10

inp = int(input())
#print(inp)
ret1 = func_plus(inp)
ret2 = func_minus(inp)
print(f"{inp} + 10 = {ret1}")
print(f"{inp} - 10 = {ret2}")