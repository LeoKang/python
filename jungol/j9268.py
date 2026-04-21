n = int(input())
# print(n)
print('\n'.join(map(str, range(n, 4, -1))))

# 1. ---------------------
N = int(input())
# print(N)

# while 5<=N:
#     print(N)
#     N -= 1 # N = N - 1

for x in range(N, 4, -1):
    print(x)
