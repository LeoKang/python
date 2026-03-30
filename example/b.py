#BJ25304
X=int(input())
A=[]
B=[]
total = 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    
for t in range(len(A)):
    total += A[t] * B[t]

print(total)

if X==total:
    print('yes')
else:
    print('no')