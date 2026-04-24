import sys
N = int(sys.stdin.readline().strip())
R = G = B = 0

for t in range(N):
    r, g, b = map(int, sys.stdin.readline().split())
    if t == 0:
        R, G, B = r, g, b
    else:
        n_R = r + min(G, B)
        n_G = g + min(R, B)
        n_B = b + min(R, G)
        R, G, B = n_R, n_G, n_B
print(min(R, G, B))
# 2. -----------------------------------
n = int(input())
# print(n)
r, g, b = map(int, input().split())

for x in range(n - 1):
    nr, ng, nb = map(int, input().split())
    
    r, g, b = nr + min(g, b), ng + min(r, b), nb + min(r, g)

print(min(r, g, b))
# 1. -----------------------------------
R = []; G = []; B = []
crdR = []; crdG = []; crdB = []
N = int(input())
for x in range(N):
    r, g, b = map(int, input().split())
    R.append(r)
    G.append(g)
    B.append(b)

crdR = R.copy()
crdG = G.copy()
crdB = B.copy()

# print(f"crdRGB -----")
# for x in range(N):
#     print(crdR[x], crdG[x], crdB[x])

for x in range(1, N):
    crdR[x] = R[x] + min(crdG[x-1], crdB[x-1])
    crdG[x] = G[x] + min(crdR[x-1], crdB[x-1])
    crdB[x] = B[x] + min(crdR[x-1], crdG[x-1])

print(f"crdRGB -----")
for x in range(N):
    print(crdR[x], crdG[x], crdB[x])

print(min(crdR[N-1], crdG[N-1], crdB[N-1]))