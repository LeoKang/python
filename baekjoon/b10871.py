a,b=map(int,input().split())
list1=list(map(int, input().split()))
hap=[]

for i in list1:
    if i<b:
        hap.append(i)

print(*hap)

# 3. --------------------------------
# N, X = map(int, input().split())
# print(N, X)
# A = input().split()
# print(A)

# # 2. --------------------------------
# res = [x for x in A if int(x)<X]
# print(*res)

# # 1. --------------------------------
# for i in range(len(A)):
#     if int(A[i]) < X:
#         print(A[i], end=' ')