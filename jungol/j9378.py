list1=list(input())

dap=list1[0::2]
print(*dap)
# 2. ----------------------------

s = input()
print(*s[::2])

# 1. ----------------------------
inp = input()
for i in range(len(inp)):
    if i%2==0:
        print(inp[i], end=' ')