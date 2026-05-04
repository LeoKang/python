stars = []
for x in range(3):
    stars.append('*') 
    print("".join(stars))

# 1. ----------------------
# N = int(input())
# print(N)

N = 3
for i in range(N):
    for j in range(i+1):
        print("*", end='')
    print()