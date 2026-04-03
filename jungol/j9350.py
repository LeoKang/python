class S:
    def __init__(self,N):
        self.N=N
    def I(self):
        if self.N>=0:
            Q.append(str(self.N))

Q=[]

for i in range(5):
    N=int(input())
    P=S(N)
    P.I()

print(f"{' '.join(Q)}")
# 2. ----------------------
elements = [int(input()) for i in range(5)]
# print(elements)
print(*elements)

# 1. ---------------------
lst = []

for i in range(5):
    x = input()
    lst.append(x)

for j in range(len(lst)):
    print(lst[j], end=' ')