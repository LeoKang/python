K = int(input())
def gap(n):
    global K
    return abs(K-n)

a, b, c = (map(int, input().split()))

print(gap(a))
print(gap(b))
print(gap(c))
# 2. -----------------------------------------
class SuperStar:
    K = 0

def GetDiff(n):
    return abs(n - SuperStar.K)

SuperStar.K = int(input())
venus = map(int, input().split())

print(*(GetDiff(x) for x in venus), sep='\n')

# 1. --------------------------------------------
K = int(input())
# print(K)
lst = list(map(int, input().split()))
# for i in range(len(lst)):
#     print(lst[i])

def k_diff(param):
    d = abs(K - param)
    return d

for i in range(3):
    ret = k_diff(lst[i])
    print(ret)