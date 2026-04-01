T = int(input())
for _ in range(T):
    R, S = input().split()

    print(*(char * int(R) for char in S), sep='')
# 4. --------------------------
T = int(input())

for _ in range(T):
    R, S = input().split()
    R = int(R)
    
    result = ""
    
    for ch in S:
        result += ch * R
    
    print(result)
# 3. -----------------------------
T = int(input())

for _ in range(T):
    R, S = input().split()
    R = int(R)

    for x in S:
        print(x*R, end='')
    
    print()

# 2. -----------------------------
T = int(input())
print(T)

lstr = []
lsts = []

for n in range(T):
    R, S = input().split()
    # print(R, S)
    lstr.append(int(R))
    lsts.append(S)

# for m in range(len(lstr)):
#     print(lstr[m], lsts[m])

for m in range(T):
    for i in lsts[m]:
        for j in range(lstr[m]):
            print(i, end='')
    print() 

# 1. ----------------------------
# T = int(input())
# # print(T)
# for n in range(T):
#     R, S = input().split()
#     # print(R, S)

#     for i in S:
#         for j in range(int(R)):
#             print(i, end='')
#     print()