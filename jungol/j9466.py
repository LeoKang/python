n=int(input())
def f():
    for i in range(1,n*n+1,1):
        if i%n!=0:
            print(i,end=' ')
        else:
            print(i)
            print()
f()

# 1. -----------------------

num = 1
def printNum():
    global num
    print(num, end=" ")
    num += 1

N = int(input())

for i in range(N):
    for j in range(N):
        printNum()
    print()