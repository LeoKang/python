class BasketSystem:
    def __init__(self, size):
        self.data = [0] * size

    def fill_range(self, i, j, k):
        for idx in range(i - 1, j):
            self.data[idx] = k

    def __str__(self):
        return " ".join(map(str, self.data))

n, m = map(int, input().split())
# print(n, m)
system = BasketSystem(n)

for _ in range(m):
    i, j, k = map(int, input().split())
    # print(i, j, k)
    system.fill_range(i, j, k)

print(system)
# 2. ------------------------------------
N, M = map(int, input().split())

list1 = [0] * N

for _ in range(M):
    i, j, k = map(int, input().split())
    
    for q in range(i, j+1):
        list1[q-1] = k

print(*list1)

# 1. ----------------------------------
N, M = map(int, input().split())
# print(N, M)

lst = list()
for row in range(N):
    lst.append(0)

for row in range(M):
    i, j, k = map(int, input().split())
    print(i, j, k)

    for x in range(i-1, j):
        lst[x] = k;

    print(*lst)