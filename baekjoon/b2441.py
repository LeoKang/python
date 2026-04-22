n = int(input())
for i in range(n,0,-1):
    print(f"{'*'*i:>{n}}")
# 2. ------------------------------
def print_stars(total, current):
    if current == total:
        return
    
    print(' ' * current + '*' * (total - current))
    
    print_stars(total, current + 1)

N_val = int(input())
# print(N_val)
print_stars(N_val, 0)

# 1. ---------------------------
N = int(input())
# print(N)

for x in range(N):
    # ? for
    for y in range(x):
        print(" ", end="")
    # * for
    for z in range(N-x, 0, -1):
        print("*", end="")
    print()